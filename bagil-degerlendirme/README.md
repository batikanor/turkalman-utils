update: see the project below by Muhammed Sihebi for a web application that does the same thing:

https://share.streamlit.io/nour0700/relative_evaluation_calculator_with_streamlit/main/main.py

http://3fcampus.tau.edu.tr/uploads/cms/oidb.tau/5690_9.pdf
a göre: (alınma tarihi 13 Haz 21)
"değişim  programlarıyla  gelen  öğrenciler,  özel  öğrenciler  ve  dersi tekrarlayan öğrenciler bağıl değerlendirme hesaplamaları dışında tutulurlar."
lütfen bu tür öğrencileri .txt den silin. Bu kod bu linkteki formülleri implemente etmektedir.


Bu kod taü yönetmeliklerine göre bağıl değerlendirme yapıyor.
.txt dosyasına inf701-2021.txt örneğindeki gibi
veya etik-guess1.txt örneğindeki gibi notları girin.
Sonra bagil.py dosyasını "python3 bagil.py" komutuyla çalıştırın.

not: tolerans değerini hocalar bizde genelde 0 alıyorlar.. (obs de 5-6 dan fazla derste hesabı denedik ve tuttu. Zamanla değişirse bilinmez. Bi zahmet bi Pull Request atın :)) 



## Örnek kod çıktısı (belirtilen sayılar ilgili notların çan eğrili dahili aralık taban değerleridir)
```
> count of grades to partake in bagil degerlendirme:  30
> average ' ' ' ':  90.0
> standard deviation ' ' ' ' 8.304547985373997
> ----------
> For tolerance value:  0  the grades will be distributed as follows:
> aa 92.636254346916
> ab 90.14488995130381
> ba 86.82307075715421
> bb 84.33170636154202
> bc 81.84034196592981
> cb 78.51852277178021
> cc 76.02715837616802
> dc 73.53579398055582
> dd 70.21397478640623
> df 67.72261039079402
> fd 66.89215559225661
> ff 0
> ------------------
> For tolerance value:  0.1  the grades will be distributed as follows:
> aa 92.29861662204472
> ab 89.80725222643251
> ba 86.48543303228291
> bb 83.99406863667072
> bc 81.50270424105852
> cb 78.18088504690891
> cc 75.68952065129672
> dc 73.19815625568452
> dd 69.87633706153493
> df 67.38497266592273
> fd 66.55451786738533
> ff 0
> ------------------
> For tolerance value:  0.2  the grades will be distributed as follows:
> aa 91.96097889717342
> ab 89.46961450156121
> ba 86.14779530741161
> bb 83.65643091179942
> bc 81.16506651618722
> cb 77.84324732203761
> cc 75.35188292642542
> dc 72.86051853081322
> dd 69.53869933666363
> df 67.04733494105142
> fd 66.21688014251403
> ff 0
> ------------------
```
