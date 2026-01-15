import requests
import matplotlib.pyplot as plt

response = requests.get("https://raw.githubusercontent.com/stivenson/students-api/master/students.json")

if response.status_code == 200:
    data = response.json()

    students_list = data['students'] 
    
    names = []
    averages = []

    for student in students_list:
        name = student['name']
        grades = student['grades'] 
        
        if len(grades) > 0:
            avg_score = sum(grades) / len(grades)
        else:
            avg_score = 0
            
        names.append(name)
        averages.append(avg_score)
        print(f"Student: {name} | Average: {avg_score:.2f}")

    plt.figure(figsize=(8, 5))
    plt.bar(names, averages, color='skyblue')
    
    plt.xlabel("Student Name")
    plt.ylabel("Average Score")
    plt.title("Student Grades Analysis")
    plt.show()

else:
    print("Error: Could not fetch data.")