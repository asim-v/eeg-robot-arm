#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver servos = Adafruit_PWMServoDriver(0x40);

unsigned int pos0 = 172; // ancho de pulso en cuentas para pocicion 0°
unsigned int pos180 = 565; // ancho de pulso en cuentas para la pocicion 180
String data;
int x, y, z, m, n, p;
void(* resetFunc) (void) = 0;



void setServo(uint8_t n_servo, int angulo) {
  int duty;
  duty = map(angulo, 0, 180, pos0, pos180);
  servos.setPWM(n_servo, 0, duty);
}

void setup() {

  
  Serial.begin(115200);
  //  Serial.setTimeout(1);
  servos.begin();
  servos.setPWMFreq(60); //Frecuecia PWM de 60Hz o T=16,66ms
  
}



void loop() {
  while (!Serial.available());

  //This line converts the input string into char
  char data_as_char[50];
  data.toCharArray(data_as_char, 50);
  data = Serial.readStringUntil('\n');

  
  if (data.equals("reset")){
    Serial.println("Resetting");
    resetFunc();
  }
  else{
  
    //This line converts char into a set of integers
    if (sscanf(data_as_char , "%d,%d,%d,%d,%d,%d", &x, &y, &z, &m, &n, &p) == 6) {
      setServo(7, 135-y);
      setServo(10, x);
      setServo(11, y);
      setServo(12, z);
      setServo(13, m);
      setServo(14, n);
      setServo(15, p);
      Serial.println("Moving servos!: " + String(x) + ',' + String(y) + ',' + String(z) + ',' + String(m) + ',' + String(n) + ',' + String(p));
    } else {
      Serial.println("Error");
    }
  }

}
