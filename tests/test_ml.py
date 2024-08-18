from movdata.ml import save_movies,save_details,save_complist,save_compdetails


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
    assert True

def test_save_complist():
    r = save_complist(2015,sleep_time=0.1)
    assert r

def test_save_compdetails():
    r = save_compdetails(2015,sleep_time=0.1)
    assert r
