from math import sqrt, atan2, asin, degrees, radians
try:
    import utime as time
except ImportError:
    import time

is_micropython = hasattr(time, 'ticks_diff')

# deltat.py time difference calculation for sensor fusion
# Released under the MIT License (MIT)
# Copyright (c) 2018 Peter Hinch
class DeltaT():
    def __init__(self, timediff):
        if timediff is None:
            self.expect_ts = False
            if is_micropython:
                self.timediff = lambda start, end : time.ticks_diff(start, end)/1000000
            else:
                raise ValueError('You must define a timediff function')
        else:
            self.expect_ts = True
            self.timediff = timediff
        self.start_time = None

    def __call__(self, ts):
        if self.expect_ts:
            if ts is None:
                raise ValueError('Timestamp expected but not supplied.')
        else:
            if is_micropython:
                ts = time.ticks_us()
            else:
                raise RuntimeError('Not MicroPython: provide timestamps and a timediff function')
        # ts is now valid
        if self.start_time is None:  # 1st call: self.start_time is invalid
            self.start_time = ts
            return 0.0001  # 100μs notional delay. 1st reading is invalid in any case

        dt = self.timediff(ts, self.start_time)
        self.start_time = ts
        return dt


# Definitions
twoKpDef = 2.0 * 5.0        # 2 * proportional gain
twoKiDef = 2.0 * 0.0        # 2 * integral gain

class MahonyFilter(object):
    def __init__(self):
        self.twoKp = twoKpDef # 2 * proportional gain (Kp)
        self.twoKi = twoKiDef # 2 * integral gain (Ki)
        self.q0 = 1.0
        self.q1 = 0.0
        self.q2 = 0.0
        self.q3 = 0.0
        self.integralFBx = 0.0
        self.integralFBy = 0.0
        self.integralFBz = 0.0
        self.deltat = DeltaT(None)

    def update(self, accel, gyro, mag=None, ts=None):
        if mag is not None:
            return update_with_mag(accel, gyro, mag, ts)
        ax, ay, az = accel
        gx, gy, gz = (radians(x) for x in gyro)
        q0 = self.q0
        q1 = self.q1
        q2 = self.q2
        q3 = self.q3

        # Compute feedback only if accelerometer measurement valid
        # (avoids NaN in accelerometer normalisation)
        if not (ax == 0.0 and ay == 0.0 and az == 0.0):
            # Normalise accelerometer measurement
            recipNorm = 1.0 / sqrt(ax * ax + ay * ay + az * az)
            ax *= recipNorm
            ay *= recipNorm
            az *= recipNorm        

            # Estimated direction of gravity and vector perpendicular to
            # magnetic flux
            halfvx = q1 * q3 - q0 * q2
            halfvy = q0 * q1 + q2 * q3
            halfvz = q0 * q0 - 0.5 + q3 * q3

            # Error is sum of cross product between estimated and measured
            # direction of gravity
            halfex = ay * halfvz - az * halfvy
            halfey = az * halfvx - ax * halfvz
            halfez = ax * halfvy - ay * halfvx

            # Compute and apply integral feedback if enabled
            if (self.twoKi > 0.0): # Difference
                # integral error scaled by Ki
                self.integralFBx += self.twoKi * halfex * deltat
                self.integralFBy += self.twoKi * halfey * deltat
                self.integralFBz += self.twoKi * halfez * deltat
                gx += self.integralFBx # apply integral feedback
                gy += self.integralFBy
                gz += self.integralFBz
            else:
                self.integralFBx = 0.0 # prevent integral windup
                self.integralFBy = 0.0
                self.integralFBz = 0.0

            # Apply proportional feedback
            gx += self.twoKp * halfex
            gy += self.twoKp * halfey
            gz += self.twoKp * halfez

        # Integrate rate of change of quaternion
        deltat = self.deltat(ts)
        gx *= 0.5 * deltat # pre-multiply common factors
        gy *= 0.5 * deltat
        gz *= 0.5 * deltat
        qa = q0
        qb = q1
        qc = q2
        q0 += (-qb * gx - qc * gy - q3 * gz)
        q1 += (qa * gx + qc * gz - q3 * gy)
        q2 += (qa * gy - qb * gz + q3 * gx)
        q3 += (qa * gz + qb * gy - qc * gx)

        # Normalise quaternion
        recipNorm = 1/sqrt(q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3)
        q0 *= recipNorm
        q1 *= recipNorm
        q2 *= recipNorm
        q3 *= recipNorm

        self.q0 = q0
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

    def update_with_mag(self, accel, gyro, mag, ts=None):
        """AHRS algorithm update"""
        mx, my, mz = mag
        ax, ay, az = accel
        gx, gy, gz = (radians(x) for x in gyro)
        q0 = self.q0
        q1 = self.q1
        q2 = self.q2
        q3 = self.q3

        # Use IMU algorithm if magnetometer measurement invalid
        # (avoids NaN in magnetometer normalisation)
        if mx == 0.0 and my == 0.0 and mz == 0.0:
            return update_nomag(self, accel, gyro, deltat)

        # Compute feedback only if accelerometer measurement valid
        # (avoids NaN in accelerometer normalisation)
        if not (ax == 0.0 and ay == 0.0 and az == 0.0):
            # Normalise accelerometer measurement
            recipNorm = 1.0 / sqrt(ax * ax + ay * ay + az * az)
            ax *= recipNorm
            ay *= recipNorm
            az *= recipNorm

            # Normalise magnetometer measurement
            recipNorm = 1.0 / sqrt(mx * mx + my * my + mz * mz)
            mx *= recipNorm
            my *= recipNorm
            mz *= recipNorm

            # Auxiliary variables to avoid repeated arithmetic
            q0q0 = q0 * q0
            q0q1 = q0 * q1
            q0q2 = q0 * q2
            q0q3 = q0 * q3
            q1q1 = q1 * q1
            q1q2 = q1 * q2
            q1q3 = q1 * q3
            q2q2 = q2 * q2
            q2q3 = q2 * q3
            q3q3 = q3 * q3

            # Reference direction of Earth's magnetic field
            hx = 2.0 * (mx * (0.5 - q2q2 - q3q3) + my * (q1q2 - q0q3) + mz * (q1q3 + q0q2))
            hy = 2.0 * (mx * (q1q2 + q0q3) + my * (0.5 - q1q1 - q3q3) + mz * (q2q3 - q0q1))
            bx = sqrt(hx * hx + hy * hy)
            bz = 2.0 * (mx * (q1q3 - q0q2) + my * (q2q3 + q0q1) + mz * (0.5 - q1q1 - q2q2))

            # Estimated direction of gravity and magnetic field
            halfvx = q1q3 - q0q2
            halfvy = q0q1 + q2q3
            halfvz = q0q0 - 0.5 + q3q3
            halfwx = bx * (0.5 - q2q2 - q3q3) + bz * (q1q3 - q0q2)
            halfwy = bx * (q1q2 - q0q3) + bz * (q0q1 + q2q3)
            halfwz = bx * (q0q2 + q1q3) + bz * (0.5 - q1q1 - q2q2)

            # Error is sum of cross product between estimated direction
            # and measured direction of field vectors
            halfex = (ay * halfvz - az * halfvy) + (my * halfwz - mz * halfwy)
            halfey = (az * halfvx - ax * halfvz) + (mz * halfwx - mx * halfwz)
            halfez = (ax * halfvy - ay * halfvx) + (mx * halfwy - my * halfwx)

            # Compute and apply integral feedback if enabled
            if (self.twoKi > 0.0): # Difference
                # integral error scaled by Ki
                self.integralFBx += self.twoKi * halfex * deltat
                self.integralFBy += self.twoKi * halfey * deltat
                self.integralFBz += self.twoKi * halfez * deltat
                gx += self.integralFBx # apply integral feedback
                gy += self.integralFBy
                gz += self.integralFBz
            else:
                self.integralFBx = 0.0 # prevent integral windup
                self.integralFBy = 0.0
                self.integralFBz = 0.0

            # Apply proportional feedback
            gx += self.twoKp * halfex
            gy += self.twoKp * halfey
            gz += self.twoKp * halfez

        deltat = self.deltat(ts)
        # Integrate rate of change of quaternion
        gx *= 0.5 * deltat # pre-multiply common factors
        gy *= 0.5 * deltat
        gz *= 0.5 * deltat
        qa = q0
        qb = q1
        qc = q2
        q0 += (-qb * gx - qc * gy - q3 * gz)
        q1 += (qa * gx + qc * gz - q3 * gy)
        q2 += (qa * gy - qb * gz + q3 * gx)
        q3 += (qa * gz + qb * gy - qc * gx)

        # Normalise quaternion
        recipNorm = 1/sqrt(q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3)
        q0 *= recipNorm
        q1 *= recipNorm
        q2 *= recipNorm
        q3 *= recipNorm

        self.q0 = q0
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

    @property
    def roll(self):
        q0 = self.q0
        q1 = self.q1
        q2 = self.q2
        q3 = self.q3
        return degrees(atan2(q0*q1 + q2*q3, 0.5 - q1*q1 - q2*q2))
    
    @property
    def pitch(self):
        q0 = self.q0
        q1 = self.q1
        q2 = self.q2
        q3 = self.q3
        return -degrees(asin(2.0 * (q1*q3 - q0*q2)))
        
    @property
    def yaw(self):
        q0 = self.q0
        q1 = self.q1
        q2 = self.q2
        q3 = self.q3
        return degrees(atan2(q1*q2 + q0*q3, q0*q0 + q1*q1 - q2*q2 - q3*q3))
