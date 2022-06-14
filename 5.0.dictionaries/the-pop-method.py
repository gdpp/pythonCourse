release_date = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}

year = release_date.pop("Java")
print(year)

if "Rust" in release_date:
    release_date.pop("Rust")
    
new_year = release_date.pop("C++", 2000)
print(new_year)