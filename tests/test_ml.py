from movdata.ml import save_movies,save_details


def test_save_movies():
    r = save_movies(2015,sleep_time=0.1)
    r = save_movies(2016,sleep_time=0.1)
    r = save_movies(2017,sleep_time=0.1)
    r = save_movies(2018,sleep_time=0.1)
    r = save_movies(2019,sleep_time=0.1)
    r = save_movies(2020,sleep_time=0.1)
    r = save_movies(2021,sleep_time=0.1)
    
    assert r 

def test_save_details():
    save_details(2015,sleep_time=0.1) 
    save_details(2016,sleep_time=0.1) 
    save_details(2017,sleep_time=0.1) 
    save_details(2018,sleep_time=0.1) 
    save_details(2019,sleep_time=0.1) 
    save_details(2020,sleep_time=0.1) 
    save_details(2021,sleep_time=0.1) 
    assert True
