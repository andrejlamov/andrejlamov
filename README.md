```
python3 main.py --cv cv.json --out out
```

```
git -C out log --all --graph --oneline --date=short --pretty=format:"%C(yellow)%h%Creset%C(red)%C(bold)%d%Creset%C(white)(%cd)%Creset %s"

* 9756dcb (HEAD -> az)(2020-01-01) Start working at Astra Zeneca
*   bc2e9cd (master)(2016-01-01) Finish working at Seal
|\  
| * 40c1f8e (seal)(2016-01-01) Start working at Seal
|/  
*   427caed(2016-01-01) Finish master thesis
|\  
| * ba57277 (chalmers)(2015-01-01) Begin master thesis
| * 6eed151(2008-01-01) Start Chalmers
* |   3f09d1a(2015-01-01) End working at Ericsson
|\ \  
| * | 93a49d3 (ericsson)(2010-01-01) Start working at Ericsson parttime
| |/  
* |   7efda22(2014-01-01) End working at Antikvariat PAN parttime
|\ \  
| |/  
|/|   
| * d5c6151 (pan)(2008-01-01) Start working at Antikvariat PAN parttime
|/  
| * 205db0f (highscool)(2004-01-01) Start highschool
|/  
* 578210a(1992-01-01) Move to Sweden
* 9b28b39(1988-09-30) Born
```
