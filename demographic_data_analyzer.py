import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    mask_male = df['sex'] == 'Male'
    
    average_age_men = round(df[mask_male].age.mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    bach_sum = len(df[df['education'] == 'Bachelors'])
    total_sum = len(df)
    
    percentage_bachelors = round((bach_sum/total_sum)*100,1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    H_edu = ['Bachelors', 'Masters', 'Doctorate']
    H_edu_df = df[df.education.isin(H_edu)]
    H_edu_rich = H_edu_df[H_edu_df['salary'] == '>50K']

    higher_education = round(len(H_edu_rich)/len(H_edu_df)*100,1)
    
    
    L_edu_df = df[~df.education.isin(H_edu)]
    L_edu_rich = L_edu_df[L_edu_df['salary'] == '>50K']
    
    lower_education = round(len(L_edu_rich)/len(L_edu_df)*100,1)

    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = lower_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_hours = df['hours-per-week'].min()
    mask_min_work = df['hours-per-week'] == min_work_hours
    
    num_min_workers = sum(mask_min_work)
    
    mask_rich = df['salary'] == '>50K'
    rich_lazy = df[mask_rich & mask_min_work]


    rich_percentage = round((len(rich_lazy)/sum(mask_min_work))*100,1)

    # What country has the highest percentage of people that earn >50K?
    
    total_by_state = df['native-country'].value_counts()
    country_list = df['native-country'].unique()
    
    
    temp = []
    
    for country in country_list:
        country_mask = df['native-country'] == country
        rich_per_country = df[country_mask & mask_rich]
        rich_precent_country = round((len(rich_per_country)/sum(country_mask))*100,1)
        temp.append([country,rich_precent_country])
    
    perc = pd.DataFrame(temp,columns=['country', 'rich_percentage'])
    rich_idx = perc['rich_percentage'].idxmax()
    
    
    highest_earning_country = perc.iloc[rich_idx].country
    highest_earning_country_percentage = perc.iloc[rich_idx].rich_percentage
    
    

    # Identify the most popular occupation for those who earn >50K in India.
    india_mask = df['native-country'] == 'India'
    india_rich_df = df[india_mask & mask_rich]
    
    occ_list = india_rich_df['occupation'].value_counts()
    
    
    top_IN_occupation = occ_list.index[0]
    


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
