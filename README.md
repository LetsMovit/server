# LetsMoviT BackEnd 구현하기 with Django



`2021.05.19`

- `accounts/signup/`  기능 구현

  - 현재 논의한 바로는 `signup`은 BackEnd에서

    `login` 은 FrontEnd에서 `JWT` 를 이용하여 구현하는 것으로.

- Detail 페이지에 대한 구상을 완료하고, 그 것을 바탕으로 모델링

<img src="README.assets/image-20210519173428352.png" alt="image-20210519173428352"  />

---

`2021.05.20`

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



