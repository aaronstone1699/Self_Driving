int m11 = 2;
int m12 = 3;
int m21 = 4;
int m22 = 5;
int dir = 0;
int ir1 = 8;
int ir3 = 6;
boolean go = false;

void setup() {

  pinMode(m11,OUTPUT);
  pinMode(m12,OUTPUT);
  pinMode(m21,OUTPUT);
  pinMode(m22,OUTPUT);
  pinMode(ir1, INPUT);
  pinMode(ir3, INPUT);
  Serial.begin(9600);

}

void loop() {
  int buttonState1 = digitalRead(ir1);
  int buttonState3 = digitalRead(ir3);
  if(go==false){
  digitalWrite(m11,HIGH);
  digitalWrite(m12,LOW);
  digitalWrite(m21,LOW);
  digitalWrite(m22,HIGH);
  delay(100);
  digitalWrite(m11,LOW);
  digitalWrite(m12,LOW);
  digitalWrite(m21,LOW);
  digitalWrite(m22,LOW);
  }
  Serial.print(buttonState1);
  Serial.print(buttonState3);
  Serial.println();
  if(Serial.available()>0){
    

    dir = Serial.read();
    if(dir == 'b'){
      go=true;

      digitalWrite(m11,HIGH);
      digitalWrite(m12,LOW);
      digitalWrite(m21,LOW);
      digitalWrite(m22,HIGH);
    }
    else if(dir == 'l'){
      go=true;

      digitalWrite(m11,HIGH);
      digitalWrite(m12,LOW);
      digitalWrite(m21,HIGH);
      digitalWrite(m22,LOW);
    }
    else if(dir == 's'){
      go=true;

      digitalWrite(m11,LOW);
      digitalWrite(m12,LOW);
      digitalWrite(m21,LOW);
      digitalWrite(m22,LOW);
    }
    else if(dir == 'r'){
      go=true;

      digitalWrite(m11,LOW);
      digitalWrite(m12,HIGH);
      digitalWrite(m21,LOW);
      digitalWrite(m22,HIGH);
    }
    else if(dir == 'f'){
      go=true;

      digitalWrite(m11,LOW);
      digitalWrite(m12,HIGH);
      digitalWrite(m21,HIGH);
      digitalWrite(m22,LOW);
    }
  
    
  }
  delay(200);
  
}
