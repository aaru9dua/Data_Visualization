<h1>STEM Vision</h1>

<h2>Overview:</h2>
    <p>STEM VISION is an interactive dashboard designed to help students navigate the domain of computer science and data science in a comprehensive manner. Our objective is to provide visual aids to students transitioning from education to industry within the domains of computer science and data science to get a glance at what various roles are and the different aspects that they need to consider a role. Through our experiments and visuals, we want to see if we can:</p>

<ol>
        <li>Create a comprehensive set of visuals that give students a sense of what a career path might entail?</li>
        <li>In particular, can we see and showcase different skills associated with a role in a meaningful and easy to understand way?</li>
        <li>Create meaningful visuals that help understand the industry landscape of that role through visualizations about top companies, salary benchmarks and preferred locations</li>
</ol>

<h2>Data:</h2>
<p>
To collect our data, we started by defining our domains- data science and computer science. We chose these domains since we were familiar with these roles and hence cross-verifying and doing any sort of qualitative analysis would be easier. Second, we choose 5 roles under each domain. We collected about 300-400 job postings from the job posting platform- Indeed.However, we ran into some issues with our scrapped data as it was very noisy. We wanted to prioritize our time for building visualizations and hence we looked at other data sources, namely, O*Net, H1b.info, and datasets made from other job platforms. 

From O*net we collected 500 job postings for each role, which gave us information about location and companies. The h1b.info dataset gave us information about salary and location. Lastly, we picked a dataset with information about job roles and skills from Naukari.com. Though Naukari.com is a job portal for India, the roles and its associated skills can be compared. </p>

The Data used for visualization is as follows:
<br>
1. Skill-Map visualization: We used Skill_Map.xlsx to create a heirachial categoires for job roles and for weighted skill map we added weights on edges using count of skill occurences (Job_vizualisation> weighted skill data og)

2. Salary Visualization:  We used merged_h1_data.csv and uscities.xlsx (present in Job_vizualisation) to create map_data.csv for creating final salary visualization. 

3. Location and Comapany Visualization: We used O*Net data for that merged with latitude and longitude information and stored in (Job_vizualisation> combined_data.csv) and to make attach logos of company in visualization we  placed the logos files as well in job_vizualisation folder.


# Final Dashbaord 

 <h2>Final Dashboard</h2>
   
<p>The final Stem vision dashboard consist of main 4 pages and the app is build on dash where the entire app structure is located in Stem_vision_dashbaord. To run our app clone the GitHub repository and use the below command-</p>

    <code>python app.py</code>
    
 <p>It will take you to <a href="http://127.0.0.1:8052/" target="_blank">http://127.0.0.1:8051/</a> port.</p>

Dash app - https://indiana-my.sharepoint.com/:f:/g/personal/shipal_iu_edu/EvkdQj1zbaVFjL0vTFumNCIB9oJkggYyyZ4MwiD5i9U6Tw?e=8h9GpK


1. Introduction Page

<img width="1440" alt="Screenshot 2023-12-08 at 3 39 31 PM" src="https://github.com/aaru9dua/Image_link/assets/46483403/b78eed08-23f8-43f5-ad9b-2f9467999b06">

2. Skill_Map by Job Title

<img width="1440" alt="Screenshot 2023-12-08 at 3 40 37 PM" src="https://github.com/aaru9dua/Image_link/assets/46483403/a149088e-c1ed-45fc-9ac0-4dadd038cbc8">

3. Visualization by 3 Job Features:

> Location
<img width="1440" alt="Screenshot 2023-12-08 at 3 41 38 PM" src="https://github.com/aaru9dua/Image_link/assets/46483403/2a91f4ed-149c-463e-8cca-09ea45835525">

>Salary

<img width="1440" alt="Screenshot 2023-12-08 at 3 44 01 PM" src="https://github.com/aaru9dua/Image_link/assets/46483403/bfcde460-58ac-4106-8b63-1acea27e176a">

>Company
<img width="1440" alt="Screenshot 2023-12-08 at 3 44 37 PM" src="https://github.com/aaru9dua/Image_link/assets/46483403/1ff74ddd-2946-4631-ba83-19541b2161a2">

4. Weighted Skill-Map
<img width="1440" alt="Screenshot 2023-12-08 at 3 45 06 PM" src="https://github.com/aaru9dua/Image_link/assets/46483403/c9d12e05-080b-469f-b6e5-5378b69fc8a8">
