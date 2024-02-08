import streamlit as st


st.title("SQL Udemy Course Analysis")
st.caption('07 February 2024')
st.caption('by Difa Fisabilillah')
st.image('https://geekflare.com/wp-content/uploads/2022/07/udemy-courses-1200x385.png', caption='Udemy Course')
st.divider()
st.markdown('''
    In today's dynamic world of online education, platforms like Udemy have emerged as a popular choice offering a vast selection of courses. Udemy boasts tens of thousands of instructors and caters to millions of students. For course administrators and data analysts, having a profound understanding of user data and course trends is essential to enhance the quality and relevance of educational content. **This article :blue[explores]  the effectiveness of SQL as a tool for extracting valuable insights from Udemy's course data**. ''')
st.header('What I Need : ')
col1, col2, col3= st.columns(3)
with col1:
# Menambahkan HTML dan CSS untuk tata letak
    st.markdown(
    """
        <style>
            .custom-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: rgba(211, 211, 211, 0.4); /* Warna abu-abu untuk background */
            padding: 30px;
            width: 250px; /* Sesuaikan lebar container sesuai kebutuhan */
            text-align: center; /* Rata tengah keterangan */
            border-radius: 8px; /* Buletkan sudut container */
        }
        .custom-container img {
            width: 50%; /* Agar gambar memenuhi lebar container */
            border-radius: 8px; /* Buletkan sudut gambar */
            margin-bottom: 10px; /* Jarak antara gambar dan keterangan */
        }
        </style>
    """
    , unsafe_allow_html=True)

# Menampilkan container berbentuk kotak dengan gambar dan keterangan
    st.markdown(
    """
        <div class="custom-container">
             <p>Data Source</p>
            <img src="https://static-00.iconduck.com/assets.00/csv-icon-896x1024-w8hg651s.png" alt="Data Source">
            <p>Data utilized originates from  <a href="https://www.kaggle.com/datasets/andrewmvd/udemy-courses" target="_blank">Kaggle</a> in flat file or CSV format </p>
        </div>
    """,unsafe_allow_html=True
)

with col2:
    # Menambahkan HTML dan CSS untuk tata letak
    st.markdown(
    """
        <style>
            .custom-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: rgba(211, 211, 211, 0.4); /* Warna abu-abu untuk background */
            padding: 15px;
            width: 150px; /* Sesuaikan lebar container sesuai kebutuhan */
            text-align: center; /* Rata tengah keterangan */
            border-radius: 8px; /* Buletkan sudut container */
        }
        .custom-container img {
            width: 50%; /* Agar gambar memenuhi lebar container */
            border-radius: 8px; /* Buletkan sudut gambar */
            margin-bottom: 10px; /* Jarak antara gambar dan keterangan */
        }
        </style>
    """
    , unsafe_allow_html=True)

# Menampilkan container berbentuk kotak dengan gambar dan keterangan
    st.markdown(
    """
        <div class="custom-container">
             <p>SQL Server 2019</p>
            <img src="https://secureservercdn.net/198.71.233.167/e2d.964.myftpupload.com/wp-content/uploads/2022/01/SSMS_Logo.jpg" alt="SQL Server 2019">
            <p>Tools for loading and exploring data sources using SQL.</p>
        </div>
    """,unsafe_allow_html=True
)
    
with col3:
    # Menambahkan HTML dan CSS untuk tata letak
    st.markdown(
    """
        <style>
            .custom-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: rgba(211, 211, 211, 0.4); /* Warna abu-abu untuk background */
            padding: 15px;
            width: 150px; /* Sesuaikan lebar container sesuai kebutuhan */
            text-align: center; /* Rata tengah keterangan */
            border-radius: 8px; /* Buletkan sudut container */
        }
        .custom-container img {
            width: 50%; /* Agar gambar memenuhi lebar container */
            border-radius: 8px; /* Buletkan sudut gambar */
            margin-bottom: 10px; /* Jarak antara gambar dan keterangan */
        }
        </style>
    """
    , unsafe_allow_html=True)

# Menampilkan container berbentuk kotak dengan gambar dan keterangan
    st.markdown(
    """
        <div class="custom-container">
             <p>Tablue</p>
            <img src="https://promto.com/wp-content/uploads/2019/08/icon-tableau-1.png" alt="Tableu Image">
            <p>Utilized for effective visualization of diverse data</p>
        </div>
    """,unsafe_allow_html=True
)
   
st.header('Data Overview')
code = '''Select * from dbo.udemy_courses'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/0.png', caption='Retrieving all data from "udemy_courses" table.')
st.markdown('''
    The following are the essential columns that contain important information: Course ID, Course Title, Paid status, Price, Subscribers, Reviews, Lectures, Level, Duration, Publish date, and Subject. ''')


st.subheader("1. How many rows and columns does the dataset have?")
code = '''select
(select count(*) from dbo.udemy_courses) As TotalRow,
(select count(*) from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'udemy_courses') As TotalColumns'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/1.png', caption='Total Row and Columns')
st.markdown('''The dataset includes 3,678 rows and 11 columns. ''')

st.subheader("2. What are the data types of each column?")
code = '''select COLUMN_NAME, data_type from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'udemy_courses'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/2.png', caption='Data Type of Each Columns.')
st.markdown('''There are 6 columns with numeric data types, 4 columns with string or categorical data types, and 1 binary column where 0 indicates course is free and 1 indicates that the course is paid''')

st.subheader("3. Is there any missing or null value in the dataset?")
code = '''SELECT
COUNT(CASE WHEN course_id is Null then 1 End) As miss_course_id,
COUNT(CASE WHEN course_title is NULL  then 1 END) As miss_course_title,
COUNT(CASE WHEN is_paid IS NULL THEN 1 END) As miss_is_paid,
COUNT(CASE WHEN price IS NULL THEN 1 END) As miss_price,
COUNT(CASE WHEN num_subscribers is NULL THEN 1 END) As miss_num_subscribers,
COUNT(CASE WHEN num_reviews is NULL THEN 1 END) As miss_num_reviews,
COUNT(CASE WHEN num_lectures is NULL THEN 1 END) miss_num_lectures,
COUNT(CASE WHEN level is NULL THEN 1 END) miss_level,
COUNT(CASE WHEN content_duration is NULL THEN 1 END) miss_content_duration,
COUNT(CASE WHEN published_timestamp is NULL THEN 1 END) miss_published_timestamp,
COUNT(CASE WHEN subject is NULL THEN 1 END) miss_subject

from dbo.udemy_courses
'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/3.png', caption='Check Missing Value.')
st.markdown('''The table does not have any missing values.''')

st.subheader("4. What are the categories present in the 'subject' and 'level' columns?")
code = '''SELECT DISTINCT subject from dbo.udemy_courses
select distinct level from dbo.udemy_courses'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/4.png', caption='Check Unique Value From Level and Subject.')
st.markdown('''In this dataset, there are four course categories: Web Development, Graphic Design, Musical Instruments, and Business Finance. The learning levels are divided into four categories as well: All levels, Beginner level, Intermediate level, and Expert level.''')

# no 5
st.subheader("5. During which years were these courses published?")
code = '''ALTER TABLE dbo.udemy_courses ADD year_published int
UPDATE dbo.udemy_courses set 
year_published=convert(int,left(published_timestamp,4))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/5.png', caption='Add year_published Column.')
st.markdown('''To add the publication year of each course in this dataset, create a "year_published" column in the "udemy_course" table. Extract the year from the "published_timestamp" column and store it in the "year_published" column.''')

code = '''SELECT DISTINCT year_published from dbo.udemy_courses Order by year_published ASC'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/5.1.png', caption='Year Published.')
st.markdown('''In this dataset, the stored course publications range from 2011 to 2017.''')

# no 6
st.subheader("6. Which subject garners the most interest based on total subscribers from 2011 to 2017?")
code = '''Select subject,SUM(num_subscribers) AS total_subscribers from dbo.udemy_courses Group By subject Order by total_subscribers Desc
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/6.png', caption='Add year_published Column.')
st.markdown('''Analyzing the overall subscriber numbers, "Web Development" stands out as the most popular subject, boasting a figure of 7,980,572, or nearly 8 million subscribers. This subject holds the top position among the other four categories, with "Business Finance" securing the second spot at a total subscriber count of 1,868,711. This suggests that 67.89% of Udemy's audience leans toward "Web Development" as their preferred subject.
''')

# no 7
st.subheader("7. What is the maximum price point in this course dataset?")
code = '''WITH rankprice AS (
    SELECT subject, price, COUNT(*) AS num_class
    FROM dbo.udemy_courses
    GROUP BY subject, price
)
SELECT *
FROM rankprice
ORDER BY price DESC;
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/7.png', caption='Maximum Price.')
st.markdown(''' Each subject has a common highest benchmark, which is 200. 
            Whether a course is deemed expensive or not could potentially impact the subject's popularity among subscribers ?
''')

# no 8
st.subheader("8. Do free classes, those with a price benchmark of 0, tend to be more popular across all subjects?")
code = '''select is_paid,sum(num_subscribers) As total_subs from dbo.udemy_courses group by is_paid
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/7.png', caption='Comparison Between Free and Paid Classes.')
st.markdown(''' Surprisingly, paid classes have more fans than free classes. 
''')


# no 9
st.subheader("9. Does the highest price benchmark for a subject in classes indicate that the subject will be less favored?")
code = '''
WITH rankprice AS (
    SELECT subject, price, COUNT(*) AS num_class, AVG(num_subscribers) As average_of_subscribers
    FROM dbo.udemy_courses
    GROUP BY subject, price
)
SELECT *
FROM rankprice
ORDER BY price DESC;
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/9.1.png', caption='Maximum Rank Price.')

code = '''
WITH rankprice AS (
    SELECT subject, price, COUNT(*) AS num_class, AVG(num_subscribers) As average_of_subscribers
    FROM dbo.udemy_courses
    GROUP BY subject, price
)
SELECT *
FROM rankprice
ORDER BY price ASC;
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/9.2.png', caption='Minimum Rank Price.')

st.markdown("Compare :")
st.image('./image/9.3.png', caption='Compare Max & Min Rank Price.')

st.markdown('''  When comparing the number of classes (num_class) and the average number of subscribers (num_of_subscribers), this comparison indeed influences the level of customer interest. Focusing on the comparison between web development with a price of 200 and web development with a price of 0, the average number of subscribers in the free web development classes is higher than those with a price tag. It's undeniable that the number of web development classes with a price tag of 0 is higher, but when comparing again, courses with a price of 0 tend to attract more audience interest. The comparison between graphic design and business finance classes with a price tag of 0 also indicates a higher attraction for free classes. However, it differs from the musical instrument subject, where the affordability of the price in the free classes and the abundance of classes do not significantly impact the level of interest. This is evident in the musical instrument class with the highest price, having more subscribers despite having fewer classes (19), compared to the 46 free classes in musical instruments.
''')
st.subheader("Price comparison can also be performed using a similar approach :")
st.markdown(" **Create View**:")

code = '''
CREATE VIEW PriceBySubs AS
SELECT subject, price,  count(*)  AS num_price, AVG(num_subscribers) AS total_Subs_Average from dbo.udemy_courses
group by subject, price;
select*from PriceBySubs'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/9.4.png', caption='View PriceBySubs.')

code = '''
WITH PriceCourse AS(
select subject, price, total_Subs_Average, 
ROW_NUMBER() OVER(PARTITION BY subject ORDER BY total_Subs_Average desc) As Rank  from dbo.PriceBySubs)
select subject, price, total_Subs_Average from PriceCourse where Rank=1;

-- MAX
with ActualPrice As(
select subject, price, total_Subs_Average, ROW_NUMBER() OVER(PARTITION BY subject ORDER BY price desc) As Rank from dbo.PriceBySubs)
select subject, price, total_Subs_Average from ActualPrice where Rank=1;
-- MIN
with ActualPrice As(
select subject, price, total_Subs_Average, ROW_NUMBER() OVER(PARTITION BY subject ORDER BY price asc) As Rank from dbo.PriceBySubs)
select subject, price, total_Subs_Average from ActualPrice where Rank=1;'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/9.5.png', caption='Comparing.')

# no 10
st.subheader("10. Is it true that free classes based on the subject class attract more subscribers' interest? ")
code = '''WITH rankprice AS (
    SELECT subject, price, COUNT(*) AS num_class, AVG(num_subscribers) As average_of_subscribers
    FROM dbo.udemy_courses
    GROUP BY subject, price
)
SELECT *
FROM rankprice
ORDER BY average_of_subscribers DESC;
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/10.png', caption='Attract More Subscribers')
st.markdown(''' Apparently not, as seen in the results above. Subjects with a price range of 170-190 have more subscribers, even though the available classes are relatively few, ranging from 2-8 classes. This could be attributed to the classes offering sought-after materials or learning content. However, when looking at the Graphic Designer subject with a price of 0 or free, it attracts more subscribers' interest compared to other subjects.
''')


# no 11
st.subheader("11. The subjects with lower popularity can be observed here. ")
code = '''WITH rankprice AS (
    SELECT subject, price, COUNT(*) AS num_price, AVG(num_subscribers) As average_of_subscribers
    FROM dbo.udemy_courses
    GROUP BY subject, price
)
SELECT *
FROM rankprice
ORDER BY average_of_subscribers ASC;
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/11.png', caption=' Lower Popularity')
st.markdown('''  
 It is evident that web development is highly appealing to users, as the smallest subscriber count for this subject is 447, with a price benchmark of 185 and a class quantity of only 2.
''')

# no 12
st.subheader("12. Check the total subscribers based on subject and year_published. ")
code = '''select year_published,subject, sum(num_subscribers) As total_subscribers  from dbo.udemy_courses group by year_published, subject order by total_subscribers Desc

))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/12.png', caption='Web Development Has Consistently Attracted User')
st.markdown('''  The subject "web development" has consistently attracted user interest for 6 consecutive years, specifically from 2013 to 2017.
''')


# no 13
st.subheader("13. Sorting by which year and subject has the least popularity? ")
st.markdown("Make rankings for each subject : ")
code = '''WITH RankCoursebySubs As(
select year_published, subject, SUM(num_subscribers) As total_subscribers,
ROW_NUMBER() OVER(PARTITION BY subject order by sum(num_subscribers)) As Rank

from dbo.udemy_courses
group by year_published, subject)

select * from RankCoursebySubs;
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/13.png', caption='Web development Has Consistently Attracted User Interest')
st.markdown(''' Grouping each subject by the year when it has the least popularity by obtaining rank 1. Where rank 1 represents the lowest number of subscribers for each subject.
''')
code = '''WITH RankCoursebySubs As(
select year_published, subject, SUM(num_subscribers) As total_subscribers,
ROW_NUMBER() OVER(PARTITION BY subject order by sum(num_subscribers)) As Rank

from dbo.udemy_courses
group by year_published, subject)

select year_published, subject, total_subscribers from RankCoursebySubs where Rank=1
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/13.1.png', caption='Web development Has Consistently Attracted User Interest')

st.markdown(''' Here, it can be observed that web development had less popularity in the year 2011, and musical instruments experienced a decline in popularity in the year 2017.
''')

# no 14
st.subheader("14. In which year did each subject experience a surge in demand? ")
code = '''WITH RankCoursebySubs As(
select year_published, subject, SUM(num_subscribers) As total_subscribers,
ROW_NUMBER() OVER(PARTITION BY subject order by sum(num_subscribers) desc) As Rank

from dbo.udemy_courses
group by year_published, subject)

select year_published, subject, total_subscribers from RankCoursebySubs where Rank=1

))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/14.png', caption='Subjects Experienced an Increase in 2015')
st.markdown('''  It turns out all four subjects experienced an increase in demand in the same year, which is in 2015.
''')

#  no 15
st.subheader("15. If based on the level, which level attracts more subscribers?  ")
code = '''select is_paid,level, sum(num_subscribers) As total_subs from dbo.udemy_courses group by is_paid, level ORDER BY total_subs DESC
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/15.png', caption='Category Attracts More Subscribers')
st.markdown('''  It turns out that the "All level" category attracts more subscribers.
''')

#  no 16
st.subheader("16. Does the number of lectures influence subscriber interest?  ")
st.markdown(" Create a View to create rankings : ")
code = '''Create view NumLecturesBySubs As
select subject, num_lectures, count(*) AS num_course, AVG(num_subscribers) AS total_Subs_Average 
from dbo.udemy_courses group by  num_lectures,subject

select * from NumLecturesBySubs
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/16.png', caption='View NumLecturesBySubs')
code = '''WITH RankSubs_AveragebyLecture AS (
select subject,num_lectures, total_Subs_Average ,ROW_NUMBER() OVER(PARTITION BY subject order by sum(total_Subs_Average) desc) As Rank
from NumLecturesBySubs group by subject,num_lectures,total_Subs_Average )
select subject,num_lectures, total_Subs_Average from RankSubs_AveragebyLecture where Rank=1;


WITH RankNumLecture AS (
select subject,num_lectures, total_Subs_Average ,ROW_NUMBER() OVER(PARTITION BY subject order by sum(num_lectures) desc) As Rank
from NumLecturesBySubs group by subject,num_lectures,total_Subs_Average )
select subject,num_lectures, total_Subs_Average from RankNumLecture where Rank=1
))'''
st.markdown("Result :")
st.image('./image/16.1.png', caption='')
st.markdown(''' When comparing the rankings based on the highest number of subscribers and the highest number of lectures, it seems that the number of lectures does not influence users to subscribe.
''')

#  no 17
st.subheader("17. The top 5 most popular course titles  ")
code = '''SELECT TOP 5 course_title,price,
level,
num_subscribers,
num_lectures,
content_duration,
subject,
year_published
FROM dbo.udemy_courses  order by num_subscribers desc
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/17.png', caption='Most Popular Course Titles')
st.markdown(''' 
The top 5 most popular course titles are from the web development subject, with "Learn HTML5 Programming from Scratch" claiming the number 1 spot.
''')

#  no 18
st.subheader("18. Create view ")
st.markdown("'**Business Finance View :** ")

code = '''CREATE VIEW BusinessFinancecourses AS select course_title,
price,
level,
num_subscribers,
num_lectures,
content_duration,
subject,
year_published 
from dbo.udemy_courses where subject='Business Finance'

select * from dbo.BusinessFinancecourses
Membuat View berdasarkan subject Business Finance
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/18.1.png', caption='BusinessFinancecourses View')

st.markdown("**Web Development View :** ")
code = '''CREATE VIEW WebDevelopmentcourses AS select course_title,
price,
level,
num_subscribers,
num_lectures,
content_duration,
subject,
year_published 
from dbo.udemy_courses where subject='Web Development'

select * from dbo.WebDevelopmentcourses

))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/18.2.png', caption='WebDevelopmentcourses View')

st.markdown("'**Graphic Design View :** ")
code = '''CREATE VIEW GraphicDesigncourses AS select course_title,
price,
level,
num_subscribers,
num_lectures,
content_duration,
subject,
year_published 
from dbo.udemy_courses where subject='Graphic Design'

select * from dbo.GraphicDesigncourses
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/18.3.png', caption='GraphicDesigncourses View')

st.markdown("'**Musical Instruments View :** ")
code = '''CREATE VIEW MusicalInstrumentscourses AS select course_title,
price,
level,
num_subscribers,
num_lectures,
content_duration,
subject,
year_published 
from dbo.udemy_courses where subject='Musical Instruments'
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/18.4.png', caption='MusicalInstrumentscourses View')

#  no 19
st.subheader("19. The most liked class in the business finance subject with a year_publish of 2016  ")
code = '''SELECT * 
FROM dbo.BusinessFinancecourses 
WHERE year_published = 2016 AND num_subscribers = (SELECT MAX(num_subscribers) FROM BusinessFinancecourses WHERE year_published = 2016);
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/19.png', caption='Most Popular Course Titles in Business Finance Subject ')
st.markdown(''' 
The most liked class in the business finance subject with a year_publish of 2016 is "The Complete Financial Analyst Course 2017." Subscribers showed a higher preference for this class in the year 2016.
''')

#  no 20
st.subheader("20. Drop unneeded columns  ")
code = '''ALTER TABLE udemy_courses DROP COLUMN published_timestamp
select * from dbo.udemy_courses
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/20.png', caption='Drop published_timestamp Column')

#  no 21
st.subheader("21. Added a new column  ")
code = '''ALTER TABLE udemy_courses ADD revenue int
UPDATE dbo.udemy_courses set revenue=price*num_subscribers
select * from dbo.udemy_courses
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/21.png', caption='Add Column Revenue')
st.markdown(''' 
A new column named revenue has been added to the table. The revenue data is obtained by multiplying the class price by the number of course subscribers. 

''')

#  no 22
st.subheader("22. What is the total and average revenue generated from publication courses during the years 2011-2017?  ")
code = '''select sum(revenue) as total_revenue, AVG(revenue) as average_revenue from dbo.udemy_courses;
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/22.png', caption='Total Average Revenue')
st.markdown(''' 
The total revenue amounts to 884,921,315 million, with an average revenue of 240,598. 

''')

#  no 23
st.subheader("23. What is the total revenue and average revenue obtained for each category per year?  ")
code = '''select year_published, sum(revenue) as total_revenue, AVG(revenue) as average_revenue 
from dbo.udemy_courses group by year_published ORDER BY year_published
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/23.png', caption='Highest Average Revenue')
st.markdown(''' 
The year 2011 is the publication year for courses with the highest average revenue.

''')
#  no 24
st.subheader("24. Average of num_subscribers & price from 2011-2017 ")
code = '''select AVG(num_subscribers) As Avg_subs from dbo.udemy_courses
select AVG(price) As Avg_price from dbo.udemy_courses
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/24.png', caption='Average of num_subscribers & price')

#  no 25
st.subheader("24. What are the titles of courses with subscriber counts and prices exceeding the average? ")
code = '''SELECT
    course_title,
subject,
level,
price,
num_subscribers,
year_published
FROM
    dbo.udemy_courses 
GROUP BY
    course_title,year_published,price,num_subscribers,subject,level
HAVING
    AVG(price) > 66
    AND MAX(num_subscribers) > 3197
ORDER BY num_subscribers DESC
))'''
st.code(code, language='sql')
st.markdown("Result :")
st.image('./image/25.png', caption='')