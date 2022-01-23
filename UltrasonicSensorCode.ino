#define trigPin1 3
#define echoPin1 2
#define trigPin2 4
#define echoPin2 5

long duration, distance, BackSensor,FrontSensor;

void setup()
{
Serial.begin (9600);
pinMode(trigPin1, OUTPUT);
pinMode(echoPin1, INPUT);
pinMode(trigPin2, OUTPUT);
pinMode(echoPin2, INPUT);

}

void loop() {
SonarSensor(trigPin1, echoPin1);
BackSensor = distance;
SonarSensor(trigPin2, echoPin2);
FrontSensor = distance;

Serial.print(FrontSensor);
Serial.print(" - ");
Serial.println(BackSensor);
}

void SonarSensor(int trigPin,int echoPin)
{
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distance = (duration/2) / 29.1;

}
