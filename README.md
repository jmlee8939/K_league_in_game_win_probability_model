# in_game_win_probability_model
 Bayesian in-game win probability model for K-league based on Pieter Robberechts's model


## K-league 실시간 승리확률 예측 모형

실시간으로 제공되는 이벤트 데이터를 활용하여, 경기 시점마다의 각 팀의 승리확률을 예측하는 모형입니다.

- Premier league 예시
![alt text](image/image.png)

### K-league LIVE EVENT 정보
- [K-league 데이터 포털](https://data.kleague.com/) 에서 실시간 이벤트 데이터 제공
    - 골 
    - 슈팅
    - 오프사이드
    - 반칙
    - 카드(경고, 퇴장)

![alt text](image/k-league_live_event.png)

### 활용한 데이터
- 활용 가능한 K-league 데이터가 없어 [Statsbomb opendata](https://github.com/statsbomb/open-data) 활용.
   - PL, La Liga, Ligue1 814경기의 event data 활용
- 전 시즌 순위 및 해당 시즌 경기 결과로 elo-rating 값 산출. 

### 모델링
- Bayesian poisson model
- 베이지안 추론 [pymc](https://www.pymc.io/welcome.html) package 활용.

### 모델 구조
- [베이지안 네트워크](graphical_structure.pdf)


### K-league 실시간 숭리확률 예측 예시
- 하나은행 K-League 4round
- 전북(홈) vs 울산(어웨이) 
- 경기일 : 2024/03/30
- 경기결과 : 2:2

![alt text](image/application_case.png)

### Reference
1. Statsbomb
2. K-League 데이터 포탈
3. Explaining Live Win Probability (LWP) - opta
4. A Bayesian Approach to In-Game Win probability in soccer(2021) P. Robberechts, Jan Van Harren, J. Davis
5. A Bayesian approach to predict football matches with changed home advantage in spectator-free matches after the COVID-19 break(2022) J Lee, J Kim, H Kim, JS Lee

