// MPU6050 connected with i2c to ESP32

#include <machine.h>

static RTC_NOINIT_ATTR int reg_b;

#define acceleration 9.81


void main () {
	uint32_t time = 1914
	measureAcceleration(time);
}

void setup() {
  // do something
}

void loop() {
  // store collected data
  // output on a display
}
