int x=0;
int pin_no=12;
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(0.1);
  pinMode(pin_no, OUTPUT);
 
}
void brightness()
{
  if(x>0){
  digitalWrite(pin_no,HIGH);
  delayMicroseconds(x*10);} // Approximately 10% duty cycle @ 1KHz
  if(x<100)
  digitalWrite(pin_no, LOW);
  delayMicroseconds(1000 - (x*10));
 }

void loop()
 {
    
    if(Serial.available())//establishment of channel
    {
      x = Serial.readString().toInt();// reads from python
      Serial.print(x);

    }
    
    brightness();
   
 }
  
