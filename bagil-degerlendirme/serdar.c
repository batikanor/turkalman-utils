// AUTHOR: SERDAR PEHLIVAN
// Use the python one instead!

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
int main(){
	FILE *fp;
	int buf,*pts;
	int i,k,ll,r;
	char *choose;
	choose=(char*)calloc(300,sizeof(char));
	pts=(int*)calloc(300,sizeof(int));
	
	recho:{}printf("dosya ismi:");scanf("%s",choose);
	if(*(choose+strlen(choose)-4)!='.'){
		strcat(choose,".txt");
	}
	fp=fopen(choose,"r");
	if(fp==NULL){
		printf("\nDosya bulunamadi\n");
		return 3;
	}
	
	rell:{}printf("BDKL(curve'ye katilacak minimum notun degeri):");scanf("%d",&ll);
	if(ll<20){
		printf("BDKL 20'den kucuk olamaz\n");goto rell;
	}
	
	for(i=0;1;i++){
		fscanf(fp," %d",&buf);
		if(buf== -1){
			break;
		}
		if(buf<ll){
			--i;r++;
		}
		else{
			*(pts+i)=buf;r++;
		}
	}
	fclose(fp);
	printf("toplam kisi sayisi:%d\n",r);
	printf("curve'ye katilacak kisi sayisi:%d\n",i);
	//end of section 1 : .txt dosyasından input okuma
	
	float n=i,avg=0,sd=0;
	
	for(k=0;k<i;k++){
	avg+=*(pts+k)/n;
	}
	
	printf("\nnotlarin ortalamasi:%.2f",avg);
	
	for(k=0;k<i;k++){
		sd+=(1/n)pow(((pts+k)-avg),2);
	}
	sd=sqrt(sd);
	printf("\nstandart sapmasi:%.2f\n",sd);
	if(!(sd>=8 && n>=20)){
		printf("can egrisi kullanilamaz\n");return 1;
	}
	//end of section 2 : ortalamanın ve standart sapmanın hesaplanması
	
	float t,c1=0.1,c2=0.2;
	float aa,ab,ba,bb,bc,cb,cc,dc,dd,df,fd,ff;
	retol:{}printf("tolerans:");scanf("%f",&t);//tolerans değişkenleri = 0,0.1,0.2
	if((t==0||t==c1||t==c2)!=1){
		printf("tolerans 0, 0.1, 0.2 degerlerinden baska bir deger alamaz\n");goto retol;
	}
	
	//custom input
	//avg=60;
	//sd=10;
	
	aa=avg+sd*(-2+(5.7-t)*(1/pow(M_E,avg/100)));
	ab=avg+sd*(-2.3+(5.7-t)*(1/pow(M_E,avg/100)));
	ba=avg+sd*(-2.7+(5.7-t)*(1/pow(M_E,avg/100)));
	bb=avg+sd*(-3+(5.7-t)*(1/pow(M_E,avg/100)));
	bc=avg+sd*(-3.3+(5.7-t)*(1/pow(M_E,avg/100)));
	cb=avg+sd*(-3.7+(5.7-t)*(1/pow(M_E,avg/100)));
	cc=avg+sd*(-4+(5.7-t)*(1/pow(M_E,avg/100)));
	dc=avg+sd*(-4.3+(5.7-t)*(1/pow(M_E,avg/100)));
	dd=avg+sd*(-4.7+(5.7-t)*(1/pow(M_E,avg/100)));
	df=avg+sd*(-5+(5.7-t)*(1/pow(M_E,avg/100)));
	fd=avg+sd*(-5.1+(5.7-t)*(1/pow(M_E,avg/100)));
	ff=0;
	printf("Harf Notlarinin Alt Limitleri:\n--------------------------------\n");
	printf("AA:%.2f\nAB:%.2f\n",aa,ab);
	printf("BA:%.2f\nBB:%.2f\nBC:%.2f\n",ba,bb,bc);
	printf("CB:%.2f\nCC:%.2f\n",cb,cc);
	printf("DC:%.2f\nDD:%.2f\nDF:%.2f\n",dc,dd,df);
	printf("FD:%.2f\nFF:%.2f",fd,ff);
	//end of section 3 : harf notlarının alt limitlerinin hesaplanması
	getchar();
	getchar();
return 2;
}