// Anomaly Detection FOMO AD servo arm
// Roni Bandini, September 2024
// MIT License
// Get serial signal from runner parser to move piece from inspection line

#include <Servo.h>

Servo myservo;  
int x;

void setup() {
  myservo.attach(3);   
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200); 
	Serial.setTimeout(1); 
  
  // led blink, device ready
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  
  // default servo position
  myservo.write(0); 
}

void loop() {

  while (!Serial.available()); 

	x = Serial.readString().toInt(); 
	Serial.print(x + 1); 

  if (x==1){  
    
      myservo.write(180);    

      delay(2000);
      myservo.write(0);                  
      delay(2000);   
  }          

}