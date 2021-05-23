# LetsMoviT BackEnd 구현하기 with Django

[2021.05.19](#2021.05.19)

- accounts, signup, Detail페이지 Prototype완성

[2021.05.20](#2021.05.20)

- User => User + Profile
- SignUp finish

[2021.05.21](#2021.05.21) 

- loaddata 실패 후,  axios로 요청해서 데이터 넣어주기
- `img` field 추가 + `$router.params.---` 로 item 가져오기
- `git merge` 순서 익히기

[2021.05.22-24](#2021.05.22-24) 

- loaddata 성공
- 

---



## 2021.05.19

- `accounts/signup/`  기능 구현

  - 현재 논의한 바로는 `signup`은 BackEnd에서

    `login` 은 FrontEnd에서 `JWT` 를 이용하여 구현하는 것으로.

- Detail 페이지에 대한 구상을 완료하고, 그 것을 바탕으로 모델링

<img src="README.assets/image-20210519173428352.png" alt="image-20210519173428352"  />

---

## 2021.05.20

- 모델링 수정과 함께 `User` 모델에 합쳐져 있던 column 들을 `User` 와 `Profile` 로 구분, 

  - 해당 과정을 진행할 때, `accounts.models.py` 에 `User` 모델이 있더라도 `Profile` 모델에서 `OneToOne` 필드로 관계설정할 때, 

    ​																													`User`를 바로참조하는 것이 아닌 `settings.AUTH_USER_MODEL` 사용

    ```python
    # accounts.models.py
    
    class User(AbstractUser):
        ...
        pass
    
    class Profile(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ```

    

- 해당 `serializers.py` 를 구성하였고, `signup`기능 마무리.

---



## 2021.05.21

- `loaddata` 로 데이터베이스를 구성하려 했으나, 생각보다 `Foreign_Key` 문제가 계속 발생해서 

  `Front` 에서 `Axios` 요청으로 DB에 주입시킴 

  ```javascript
  methods: {
      getData: function () {
        for (let index = 0; index < movies.length; index++) {
          const element = movies[index]
          if (element.model === 'movies.movie') {
            const data = element.fields
  
            axios.post('http://127.0.0.1:8000/movies/', {
              title: data.title,
              overview: data.overview,
              poster_path: data.poster_path,
              backdrop_path: data.backdrop_path,
              vote_average: data.vote_average,
              movie_id: data.movie_id,
            })
              .then((res)=> {
                // store 에 저장
                console.log(res)
                this.$store.dispatch('saveMovieList', res.data)
              })
              .catch((err)=> {
                console.log(err)
              })
          }
        }      
      }
    },
    created: function () {
      this.getData()
    }
  ```

  

- ### Parameter Params 받아오기

  ```python
  <button class="btn btn-primary" @click="goDetail(movie)">Go somewhere</button>
  methods: {
      goDetail: function (movie) {
        this.$router.push({ name: 'MovieDetail', params: {item : movie} })
      }
    }
  #================================================================================
  <div>
      {{ this.$route.params.item }}
      <Location/>
  </div>
  
  ```

- ### Git Merge 순서

  - `git branch feature_A`    

    - 브랜치 `feature_A` 를 만들고 변경사항을 기록한 후 , `add` , `commit`, `push`  진행

  - `git pull feature_A` 

    - 다른 merge 하고자 하는 곳에서 `pull` 땡기면, `conflicts` 발생하면 `conflicts` 제거 후에 

      `add` , `commit` , `push` 

  

---

## 2021.05.22-24

- 결국 loaddata를 해결했다. 

  - 가장 문제시 됐던 건, `M:N` 필드를 설정할 때 과연 로드데이터가 어떤 식으로 형성이 되는가 였다.

    나는 `M:N` 이기 때문에 양쪽필드에 각 `id`  에 해당하는 값들을 list로 넣어주면 되겠다 생각했지만 

    결론적으로 이야기하자면 `M:N` 필드를 선언한 모델에만 해당 `column`이름을 기준으로 `list` 형식으로 넣어주면 된다.

    정말 너무 많은 시간을 소비했다 .. 하지만 해결해서 너무 뿌듯하다.

- `Vue.js` 에 `CommentForm` 컴포넌트를 만들었다. 해당 컴포넌트에서는 **이미지**를 받아야하는 상황이었기에

  ```javascript
  <button class="btn btn-primary" @click.prevent="createComment">Submit</button>
  ...
  handleFileChange(e) {
        // Whenever the file changes, emit the 'input' event with the file data.
        // this.$emit('input', e.target.files[0])
        this.image = e.target.files[0]            
      }
  ```

  으로 처리하였다. 

- 추가로 별점을 줘야하는 `rating`은 `vue-star-rating` 라이브러리를 사용해서 구현하였다.

