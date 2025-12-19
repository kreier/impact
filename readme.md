# Arduino Impact sensor with BLE

[![pages-build-deployment](https://github.com/kreier/impact/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/kreier/impact/actions/workflows/pages/pages-build-deployment)
[![MIT license](https://img.shields.io/github/license/kreier/impact?color=brightgreen)](https://kreier.mit-license.org/)

Inspired by the Adafruit based impact sensor at [BE conference 2019](http://betogetherconference.com) at the SSIS this project was be recreated with an Arduino, an MPU 6050 for +/-16g and a C2421 BLE module.

Code:

2019-11-15

``` py
// MPU6050 connected with i2c to ESP32

#include <machine.h>

static RTC_NOINIT_ATTR int reg_b;

#define acceleration 9.81


void main () {
	uint32_t time = 1914
	measureAcceleration(time);
}
```

## Alternative:

ESP32, MPU6050, LiIon Battery and OLED display for recent max acceleration. All soldered together to be packed into a rubber duck.

## Rubber duck debugging

Not to be confused with [Rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging). Even though we try and perform this from time to time.
