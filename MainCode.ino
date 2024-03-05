#include <SoftwareSerial.h>


#define XSTEP 2 //pulse
#define YSTEP 3 //pulse
#define ZSTEP 4 //pulse
#define XDIR 5 //direction
#define YDIR 6 //direction
#define ZDIR 7 //direction
#define ENCNC 8 //enable run numStep

#define XLIMIT A0
#define YLIMIT A1
#define ZLIMIT A2

#define YTOPICK 1000
#define ZTOPICK 2700

#define XTOACTIVE 2300
#define XTOCOL 2000

#define ZTOACTIVE 8200
#define ZTOROW 10000

#define SRX 10
#define STX 11

byte UARTData[2];
byte UARTIndex=0;

byte CurrentCol=0;
byte CurrentRow=0;

SoftwareSerial DataSerial(SRX,STX);

void ZGoHome()
{
  digitalWrite(ZDIR,LOW);
  while(digitalRead(ZLIMIT)==HIGH)
  {
    digitalWrite(ZSTEP,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(ZSTEP,LOW); 
    delayMicroseconds(500); 
  }
}

void XGoHome()
{
  digitalWrite(XDIR,LOW);
  while(digitalRead(XLIMIT)==HIGH)
  {
    digitalWrite(XSTEP,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(XSTEP,LOW); 
    delayMicroseconds(500); 
  }
}

void YGoHome()
{
  digitalWrite(YDIR,HIGH);
  while(digitalRead(YLIMIT)==HIGH)
  {
    digitalWrite(YSTEP,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(YSTEP,LOW); 
    delayMicroseconds(500); 
  }
  
}


void YPick()
{
  int Step;
  digitalWrite(YDIR,LOW);
  for(Step=0;Step<YTOPICK;Step++)
  {
    digitalWrite(YSTEP,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(YSTEP,LOW); 
    delayMicroseconds(500); 
  }
}

void ZPick()
{
  int Step;
  digitalWrite(ZDIR,HIGH);
  for(Step=0;Step<ZTOPICK;Step++)
  {
    digitalWrite(ZSTEP,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(ZSTEP,LOW); 
    delayMicroseconds(500); 
  }
}

void ZRelease()
{
  int Step;
  digitalWrite(ZDIR,LOW);
  for(Step=0;Step<ZTOPICK;Step++)
  {
    digitalWrite(ZSTEP,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(ZSTEP,LOW); 
    delayMicroseconds(500); 
  }
}

void XGotoActive()
{
  int Step;
  digitalWrite(XDIR,HIGH);
  for(Step=0;Step<XTOACTIVE;Step++)
  {
    digitalWrite(XSTEP,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(XSTEP,LOW); 
    delayMicroseconds(500); 
  }
  CurrentCol=1;
}

void XGotoCol(byte Col)
{
  int Step;
  int StepRun;
  if(Col<CurrentCol)
  {
    digitalWrite(XDIR,LOW);
    StepRun=(CurrentCol-Col)*XTOCOL;
  }
  else
  {
    digitalWrite(XDIR,HIGH);
    StepRun=(Col-CurrentCol)*XTOCOL;
  }
  
   for(Step=0;Step<StepRun;Step++)
  {
    digitalWrite(XSTEP,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(XSTEP,LOW); 
    delayMicroseconds(500); 
  }
  CurrentCol=Col;
}

void ZGotoActive()
{
  int Step;
  digitalWrite(ZDIR,HIGH);
  for(Step=0;Step<ZTOACTIVE;Step++)
  {
    digitalWrite(ZSTEP,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(ZSTEP,LOW); 
    delayMicroseconds(500); 
  }
  CurrentRow=1;
}

void ZGotoRow(byte Row)
{
  int Step;
  int StepRun;
  if(Row<CurrentRow)
  {
    digitalWrite(ZDIR,LOW);
    StepRun=(CurrentRow-Row)*ZTOROW;
  }
  else
  {
    digitalWrite(ZDIR,HIGH);
    StepRun=(Row-CurrentRow)*ZTOROW;
  }
  
   for(Step=0;Step<StepRun;Step++)
  {
    digitalWrite(ZSTEP,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(ZSTEP,LOW); 
    delayMicroseconds(500); 
  }
  CurrentRow=Row;
}

void PutObjectHome()
{
  XGoHome();
  YPick();
  ZGoHome();
  YGoHome();
}

void PutObjectToLocation(byte Location)
{
  int Row;
  int Col;
  Location=10-Location;// dao nguoc vi tri theo so slot tren phan mem)
  
  Row=(Location-1)/3+1;
  Col=((Location-1)%3)+1;
  YPick();
  ZPick();
  YGoHome();
  ZGotoActive();
  ZGotoRow(Row);
  XGotoActive();
  XGotoCol(Col);
  YPick();
  ZRelease();
  YGoHome();
  XGoHome();
  ZGoHome();
}

void GetObjectFromLocation(byte Location)
{
  int Row;
  int Col;
  Location=10-Location;// dao nguoc vi tri theo so slot tren phan mem)
  Row=(Location-1)/3+1;
  Col=((Location-1)%3)+1;
  ZGotoActive();
  ZGotoRow(Row);
  XGotoActive();
  XGotoCol(Col);
  YPick();
  ZPick();
  YGoHome();
  XGoHome();
  YPick();
  ZGoHome();
  YGoHome();
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  DataSerial.begin(9600);
  pinMode(XSTEP,OUTPUT);
  pinMode(YSTEP,OUTPUT);
  pinMode(ZSTEP,OUTPUT);
  pinMode(XDIR,OUTPUT);
  pinMode(YDIR,OUTPUT);
  pinMode(ZDIR,OUTPUT);
  pinMode(ENCNC,OUTPUT);
  digitalWrite(ENCNC,LOW);
  pinMode(XLIMIT,INPUT_PULLUP);
  pinMode(YLIMIT,INPUT_PULLUP);
  pinMode(ZLIMIT,INPUT_PULLUP);
  
  YGoHome();
  XGoHome();
  ZGoHome();
  
}

void loop() {
  // put your main code here, to run repeatedly:
  byte SData;

  if(DataSerial.available())
  {
    SData=DataSerial.read();
    UARTData[UARTIndex]=SData;
    
    if(SData==0x0D) 
    {
      UARTIndex=0;
      UARTData[0]=UARTData[0]-0x30; //covert assi to number
      if(UARTData[0]<10) PutObjectToLocation(UARTData[0]);
      Serial.write(0xB0+UARTData[0]); // gui lenh len app
      while(DataSerial.available()) SData=DataSerial.read();// xoa bo nho dem uart
    }
    else
    {
      UARTIndex++;
    }
     
  }
  if(Serial.available())
  {
    SData=Serial.read();
    if(SData<=0xA9&&SData>=0xA1)
    {
      GetObjectFromLocation(SData-0xA0);
    }
  }
  

}
