{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p style=\"text-align:center\">\n",
    "    <a href=\"https://skills.network\" target=\"_blank\">\n",
    "    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"200\" alt=\"Skills Network Logo\">\n",
    "    </a>\n",
    "</p>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **Collecting Job Data Using APIs**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Estimated time needed: **45 to 60** minutes\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Objectives\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "After completing this lab, you will be able to:\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*   Collect job data from GitHub Jobs API\n",
    "*   Store the collected data into an excel spreadsheet.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "><strong>Note: Before starting with the assignment make sure to read all the instructions and then move ahead with the coding part.</strong>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Instructions\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To run the actual lab, firstly you need to click on the [Jobs_API](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/Jobs_API.ipynb) notebook link. The file contains flask code which is required to run the Jobs API data.\n",
    "\n",
    "Now, to run the code in the file that opens up follow the below steps.\n",
    "\n",
    "Step1: Download the file. \n",
    "\n",
    "Step2: Upload it on the IBM Watson studio. (If IBM Watson Cloud service does not work in your system, follow the alternate Step 2 below)\n",
    "\n",
    "Step2(alternate): Upload it in your SN labs environment using the upload button which is highlighted in red in the image below:\n",
    "Remember to upload this Jobs_API file in the same folder as your current .ipynb file\n",
    "\n",
    "<img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/Upload.PNG\">\n",
    "\n",
    "Step3:  Run all the cells of the Jobs_API file. (Even if you receive an asterik sign after running the last cell, the code works fine.)\n",
    "\n",
    "If you want to learn more about flask, which is optional, you can click on this link [here](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/FLASK_API.md.html).\n",
    "\n",
    "Once you run the flask code, you can start with your assignment.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Dataset Used in this Assignment\n",
    "\n",
    "The dataset used in this lab comes from the following source: https://www.kaggle.com/promptcloud/jobs-on-naukricom under the under a **Public Domain license**.\n",
    "\n",
    "> Note: We are using a modified subset of that dataset for the lab, so to follow the lab instructions successfully please use the dataset provided with the lab, rather than the dataset from the original source.\n",
    "\n",
    "The original dataset is a csv. We have converted the csv to json as per the requirement of the lab.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Warm-Up Exercise\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Before you attempt the actual lab, here is a fully solved warmup exercise that will help you to learn how to access an API.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using an API, let us find out who currently are on the International Space Station (ISS).<br> The API at [http://api.open-notify.org/astros.json](http://api.open-notify.org/astros.json?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2021-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ) gives us the information of astronauts currently on ISS in json format.<br>\n",
    "You can read more about this API at [http://open-notify.org/Open-Notify-API/People-In-Space/](http://open-notify.org/Open-Notify-API/People-In-Space?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2021-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import requests # you need this module to make an API call\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "api_url = \"http://api.open-notify.org/astros.json\" # this url gives use the astronaut data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "response = requests.get(api_url) # Call the API using the get method and store the\n",
    "                                # output of the API call in a variable called response."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "if response.ok:             # if all is well() no errors, no network timeouts)\n",
    "    data = response.json()  # store the result in json format in a variable called data\n",
    "                            # the variable data is of type dictionary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'people': [{'craft': 'ISS', 'name': 'Oleg Kononenko'}, {'craft': 'ISS', 'name': 'Nikolai Chub'}, {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}, {'craft': 'ISS', 'name': 'Matthew Dominick'}, {'craft': 'ISS', 'name': 'Michael Barratt'}, {'craft': 'ISS', 'name': 'Jeanette Epps'}, {'craft': 'ISS', 'name': 'Alexander Grebenkin'}, {'craft': 'ISS', 'name': 'Butch Wilmore'}, {'craft': 'ISS', 'name': 'Sunita Williams'}, {'craft': 'Tiangong', 'name': 'Li Guangsu'}, {'craft': 'Tiangong', 'name': 'Li Cong'}, {'craft': 'Tiangong', 'name': 'Ye Guangfu'}], 'number': 12, 'message': 'success'}\n"
     ]
    }
   ],
   "source": [
    "print(data)   # print the data just to check the output or for debugging"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Print the number of astronauts currently on ISS.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "print(data.get('number'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Print the names of the astronauts currently on ISS.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 12 astronauts on ISS\n",
      "And their names are :\n",
      "Oleg Kononenko\n",
      "Nikolai Chub\n",
      "Tracy Caldwell Dyson\n",
      "Matthew Dominick\n",
      "Michael Barratt\n",
      "Jeanette Epps\n",
      "Alexander Grebenkin\n",
      "Butch Wilmore\n",
      "Sunita Williams\n",
      "Li Guangsu\n",
      "Li Cong\n",
      "Ye Guangfu\n"
     ]
    }
   ],
   "source": [
    "astronauts = data.get('people')\n",
    "print(\"There are {} astronauts on ISS\".format(len(astronauts)))\n",
    "print(\"And their names are :\")\n",
    "for astronaut in astronauts:\n",
    "    print(astronaut.get('name'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Hope the warmup was helpful. Good luck with your next lab!\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Lab: Collect Jobs Data using GitHub Jobs API\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Objective: Determine the number of jobs currently open for various technologies  and for various locations\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Collect the number of job postings for the following locations using the API:\n",
    "\n",
    "* Los Angeles\n",
    "* New York\n",
    "* San Francisco\n",
    "* Washington DC\n",
    "* Seattle\n",
    "* Austin\n",
    "* Detroit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#Import required libraries\n",
    "import pandas as pd\n",
    "import json\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Write a function to get the number of jobs for the Python technology.<br>\n",
    "> Note: While using the lab you need to pass the **payload** information for the **params** attribute in the form of **key** **value** pairs.\n",
    "  Refer the ungraded **rest api lab** in the course **Python for Data Science, AI & Development**  <a href=\"https://www.coursera.org/learn/python-for-applied-data-science-ai/ungradedLti/P6sW8/hands-on-lab-access-rest-apis-request-http?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01\">link</a>\n",
    "  \n",
    " ##### The keys in the json are \n",
    " * Job Title\n",
    " \n",
    " * Job Experience Required\n",
    " \n",
    " * Key Skills\n",
    " \n",
    " * Role Category\n",
    " \n",
    " * Location\n",
    " \n",
    " * Functional Area\n",
    " \n",
    " * Industry\n",
    " \n",
    " * Role \n",
    " \n",
    "You can also view  the json file contents  from the following <a href = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json\">json</a> URL.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "api_url=\"http://127.0.0.1:5000/data\"\n",
    "def get_number_of_jobs_T(technology):\n",
    "    payload = {\"Key Skills\": technology}\n",
    "    response = requests.get(api_url, params = payload)\n",
    "    if response.ok:\n",
    "        data = response.json()\n",
    "        number_of_jobs = len(data)\n",
    "    \n",
    "    #your code goes here\n",
    "    return technology,number_of_jobs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calling the function for Python and checking if it works.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('Java', 2609)"
      ]
     },
     "execution_count": 179,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "get_number_of_jobs_T(\"Java\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Write a function to find number of jobs in US for a location of your choice\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    " def get_number_of_jobs_L(location):\n",
    "    payload = {\"Location\":location}\n",
    "    response = requests.get(api_url, params = payload)\n",
    "    if response.ok:\n",
    "        data = response.json()\n",
    "        number_of_jobs = len(data)\n",
    "    #your coe goes here\n",
    "    return location,number_of_jobs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call the function for Los Angeles and check if it is working.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('Los Angeles', 640)"
      ]
     },
     "execution_count": 181,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#your code goes here\n",
    "get_number_of_jobs_L(\"Los Angeles\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Store the results in an excel file\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call the API for all the given technologies above and write the results in an excel spreadsheet.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you do not know how create excel file using python, double click here for **hints**.\n",
    "\n",
    "<!--\n",
    "\n",
    "from openpyxl import Workbook        # import Workbook class from module openpyxl\n",
    "wb=Workbook()                        # create a workbook object\n",
    "ws=wb.active                         # use the active worksheet\n",
    "ws.append(['Country','Continent'])   # add a row with two columns 'Country' and 'Continent'\n",
    "ws.append(['Eygpt','Africa'])        # add a row with two columns 'Egypt' and 'Africa'\n",
    "ws.append(['India','Asia'])          # add another row\n",
    "ws.append(['France','Europe'])       # add another row\n",
    "wb.save(\"countries.xlsx\")            # save the workbook into a file called countries.xlsx\n",
    "\n",
    "\n",
    "-->\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a python list of all technologies for which you need to find the number of jobs postings.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#your code goes here\n",
    "technologies =[\"Python\",\"C#\",\"Java\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Import libraries required to create excel spreadsheet\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#!pip install openpyxl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# your code goes here\n",
    "#from openpyxl import Workbook"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a workbook and select the active worksheet\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# your code goes here\n",
    "wb=Workbook()\n",
    "ws=wb.active\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Find the number of jobs postings for each of the technology in the above list.\n",
    "Write the technology name and the number of jobs postings into the excel spreadsheet.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "for i in technologies:\n",
    "    ws.append(get_number_of_jobs_T(i))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Save into an excel spreadsheet named 'github-job-postings.xlsx'.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "wb.save('github-job-posting.xlsx')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### In the similar way, you can try for below given technologies and results  can be stored in an excel sheet.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Collect the number of job postings for the following languages using the API:\n",
    "\n",
    "*   C\n",
    "*   C#\n",
    "*   C++\n",
    "*   Java\n",
    "*   JavaScript\n",
    "*   Python\n",
    "*   Scala\n",
    "*   Oracle\n",
    "*   SQL Server\n",
    "*   MySQL Server\n",
    "*   PostgreSQL\n",
    "*   MongoDB\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# your code goes here\n",
    "technologies_2 =[\"C\",\"C#\",\"C++\",\"Java\",\"JavaScript\",\"Python\",\"Scala\",\"Oracle\",\"SQL Server\",\"MySQL Server\",\"PostgreSQL\",\"MongoDB\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# your code goes here\n",
    "wb=Workbook()\n",
    "ws=wb.active"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "for i in technologies_2:\n",
    "    ws.append(get_number_of_jobs_T(i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "wb.save('github-New-job-posting.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               C  13498\n",
      "0             C#    333\n",
      "1            C++    305\n",
      "2           Java   2609\n",
      "3     JavaScript    355\n",
      "4         Python   1173\n",
      "5          Scala     33\n",
      "6         Oracle    784\n",
      "7     SQL Server    250\n",
      "8   MySQL Server      0\n",
      "9     PostgreSQL     10\n",
      "10       MongoDB    174\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<function matplotlib.pyplot.show(close=None, block=None)>"
      ]
     },
     "execution_count": 202,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABRsAAAK7CAYAAAByAFjQAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/NK7nSAAAACXBIWXMAAA9hAAAPYQGoP6dpAABq6klEQVR4nO3dd5gUVdo/7mdIw5BzlCQImACzwCrwGjAh5qygq8saMKxrTqAiZvmurroGwBzWtKjoq6KsrhkREwoGUHYFWVDBBCic3x/+pl+bGWBGC4bR+76uvqBPVVc/dbq6uvszVXUKUkopAAAAAAB+oSoVXQAAAAAA8OsgbAQAAAAAMiFsBAAAAAAyIWwEAAAAADIhbAQAAAAAMiFsBAAAAAAyIWwEAAAAADIhbAQAAAAAMiFsBAAAAAAyIWwEgEpm7NixUVBQEJMmTSrX44YNGxYFBQUxb9681VTZr9PUqVNj2LBhMXPmzBLTBg8eHO3bt1/jNa2NZs6cGbvuums0atQoCgoK4sQTT6zokjLTvn37GDx4cEWXUarx48fHsGHDVvvzDB48OOrUqbPan6c0xfu80t6DWSooKFgjfQkAv3bVKroAAIC12dSpU2P48OHRt29fweJKnHTSSfHyyy/H6NGjo0WLFtGyZcuKLikzDz74YNSrV6+iyyjV+PHj469//auQLAMvvvhirLPOOhVdBgBUesJGAKDS+P7776OgoCCqVSv5Febbb7+NWrVqVUBVRES8/fbbseWWW8Yee+yRyfKWLl0aP/zwQxQWFmayvJ/ju+++i6Kiothkk00qrAbWnK233rqiSwCAXwWnUQPAr8C4ceOiZ8+eUatWrahbt27ssMMO8eKLL5Y676xZs2KvvfaKevXqRf369eOQQw6J//73v3nzPP3009G3b99o3LhxFBUVRdu2bWPvvfeOb7/9dpW13HnnndGzZ8+oU6dO1KlTJ3r06BE333xzbvqKTknt27dv9O3bN3d/4sSJUVBQELfddlucfPLJ0bp16ygsLIwPPvggd0rnW2+9FTvuuGPUrVs3tttuu4iIWLJkSVx44YXRtWvXKCwsjKZNm8bhhx9eYh3bt28fu+22Wzz++OOx6aabRlFRUXTt2jVGjx6dm2fs2LGx7777RkREv379oqCgIAoKCmLs2LGlrvt2220XXbt2jZRSXntKKTp16hS77rrrSvtu2bJlcemll+Zqb9asWRx22GHx73//u0RfbbTRRvHcc8/F1ltvHUVFRdG6des455xzYunSpXnzZtkfpSl+nT744IN47LHHcn1UfMrrJ598Eoccckg0a9YsCgsLY/31148rrrgili1bllvGzJkzo6CgIC699NK48MILo0OHDlFYWBjPPPNMqc+5ySabxDbbbFOifenSpdG6devYa6+9cm3Dhw+PrbbaKho1ahT16tWLTTfdNG6++eYSr1Hx+j/wwAOxySabRM2aNWP48OG5actvs2VZr+K+mThxYt5ji9f3p9vRRx99FAcccEC0atUqCgsLo3nz5rHddtvFlClTVtT1MXjw4PjrX/8aEZHr95/2fUoprr322ujRo0cUFRVFw4YNY5999omPPvqoxLIef/zx2G677aJ+/fpRq1atWH/99WPkyJEl5vvggw9il112iTp16kSbNm3i5JNPjsWLF5dYt8svvzyuvPLK6NChQ9SpUyd69uwZL730UonllWfftbzRo0dH9+7do2bNmtGoUaPYc88949133y0x34033hidO3eOwsLC2GCDDeLOO+8s9RIIpZ1GPWfOnBgyZEiss846UaNGjejQoUMMHz48fvjhh7z5rrvuuujevXvUqVMn6tatG127do0zzzyzTOsBAL82jmwEgEruzjvvjIMPPjh23HHHuOuuu2Lx4sVx6aWXRt++fWPChAnxu9/9Lm/+PffcM/bbb7/44x//GO+8806cc845MXXq1Hj55ZejevXquWvvbbPNNjF69Oho0KBB/Oc//4nHH388lixZstKjB88999y44IILYq+99oqTTz456tevH2+//XZ8/PHHP3v9zjjjjOjZs2dcf/31UaVKlWjWrFlE/Bii7b777jFkyJA4/fTT44cffohly5bFwIED47nnnotTTz01evXqFR9//HGcd9550bdv35g0aVIUFRXllv3GG2/EySefHKeffno0b948brrppvj9738fnTp1im233TZ23XXXuOiii+LMM8+Mv/71r7HppptGRETHjh1LrfWEE06IgQMHxoQJE2L77bfPtT/22GPx4Ycfxl/+8peVruvRRx8dN9xwQxx33HGx2267xcyZM+Occ86JiRMnxuTJk6NJkya5eefMmRMHHHBAnH766XH++efHo48+GhdeeGF88cUXcc0110REZN4fpdl0003jxRdfjD333DM6duwYl19+eUREtGzZMv773/9Gr169YsmSJXHBBRdE+/bt45FHHok///nP8eGHH8a1116bt6y//OUv0blz57j88sujXr16sd5665X6nIcffniccMIJ8f777+fN88QTT8Snn34ahx9+eK5t5syZMWTIkGjbtm1ERLz00ksxdOjQ+M9//hPnnntu3nInT54c7777bpx99tnRoUOHqF27dqnPX971Kotddtklli5dGpdeemm0bds25s2bFy+88EJ8+eWXK3zMOeecE998803cd999eQFd8SnsQ4YMibFjx8bxxx8fl1xySXz++edx/vnnR69eveKNN96I5s2bR0TEzTffHEcddVT06dMnrr/++mjWrFlMnz493n777bzn+/7772P33XeP3//+93HyySfHs88+GxdccEHUr1+/RF/+9a9/ja5du8aoUaNyte6yyy4xY8aMqF+/fkSUf9/1UyNHjowzzzwzDjzwwBg5cmTMnz8/hg0bFj179oxXX301t13ccMMNMWTIkNh7773jqquuigULFsTw4cPzAtIVmTNnTmy55ZZRpUqVOPfcc6Njx47x4osvxoUXXhgzZ86MMWPGRETE3XffHcccc0wMHTo0Lr/88qhSpUp88MEHMXXq1FU+BwD8KiUAoFIZM2ZMioj06quvpqVLl6ZWrVqljTfeOC1dujQ3z1dffZWaNWuWevXqlWs777zzUkSkk046KW95d9xxR4qIdPvtt6eUUrrvvvtSRKQpU6aUq66PPvooVa1aNR188MErna9du3Zp0KBBJdr79OmT+vTpk7v/zDPPpIhI2267bYl5Bw0alCIijR49Oq/9rrvuShGR7r///rz2V199NUVEuvbaa/PqqFmzZvr4449zbd99911q1KhRGjJkSK7t73//e4qI9Mwzz5RaR7t27XL3ly5dmtZdd900cODAvPl23nnn1LFjx7Rs2bISyyj27rvvpohIxxxzTF77yy+/nCIinXnmmbm2Pn36pIhI//jHP/LmPeqoo1KVKlVy67Q6+mNF2rVrl3bddde8ttNPPz1FRHr55Zfz2o8++uhUUFCQpk2bllJKacaMGSkiUseOHdOSJUtW+Vzz5s1LNWrUyOuTlFLab7/9UvPmzdP3339f6uOWLl2avv/++3T++eenxo0b570e7dq1S1WrVs3VtPy6/XSbLet6FW/Dy287xes7ZsyY3PpERBo1atQq1315xx57bCrtK/2LL76YIiJdccUVee2zZs1KRUVF6dRTT00p/bivqFevXvrd73630u2z+D1377335rXvsssuqUuXLiXWbeONN04//PBDrv2VV15JEZHuuuuulFIq176reJ83Y8aMlFJKX3zxRSoqKkq77LJLXi2ffPJJKiwsTAcddFDuOVq0aJG22mqrvPk+/vjjVL169bz3bkopRUQ677zzcveHDBmS6tSpk/eeSCmlyy+/PEVEeuedd1JKKR133HGpQYMGK+w7APitcRo1AFRi06ZNi08//TQOPfTQqFLl/z7W69SpE3vvvXe89NJLJU59Pvjgg/Pu77ffflGtWrXcKas9evSIGjVqxB/+8Ie45ZZbSj3lsjRPPvlkLF26NI499thfuFb59t577zJPe+SRR6JBgwYxYMCA+OGHH3K3Hj16RIsWLUqcztqjR4/cEW8RETVr1ozOnTv/7CMxq1SpEscdd1w88sgj8cknn0RExIcffhiPP/54HHPMMVFQULDCxxb3//Kn62655Zax/vrrx4QJE/La69atG7vvvnte20EHHRTLli2LZ599NiIqvj+efvrp2GCDDWLLLbfMax88eHCklOLpp5/Oa999992jevXqq1xu48aNY8CAAXHLLbfkTlv+4osv4h//+Eccdthhedf0fPrpp2P77beP+vXrR9WqVaN69epx7rnnxvz582Pu3Ll5y+3WrVt07tw58/ValUaNGkXHjh3jsssuiyuvvDJef/31vNOxf45HHnkkCgoK4pBDDsl77Vu0aBHdu3fPvfYvvPBCLFy4cJXbZ8SPpxkPGDAgr61bt26lbh+77rprVK1aNW++iMjN+3P2XcVefPHF+O6770q8V9q0aRP/8z//k3uvTJs2LebMmRP77bdf3nxt27aN3r17r3RdI37sw379+kWrVq3y+nDnnXeOiIh//vOfEfHje/TLL7+MAw88MP7xj3/EvHnzVrlsAPg1EzYCQCU2f/78iIhSR/5t1apVLFu2LL744ou89hYtWuTdr1atWjRu3Di3rI4dO8ZTTz0VzZo1i2OPPTY6duwYHTt2jP/3//7fSmspvgZg1qO5rmhU41q1apUYIfizzz6LL7/8MmrUqBHVq1fPu82ZM6dECNC4ceMSyy0sLIzvvvvuZ9d7xBFHRFFRUVx//fUR8ePppEVFRXHEEUes9HGrei2LpxcrPgX2p4pf2+J5K7o/5s+fv8L1+WmdxcozgvURRxwR//nPf+LJJ5+MiMidhvvTAOqVV16JHXfcMSJ+vG7f888/H6+++mqcddZZEREl1qusz1/e9VqVgoKCmDBhQvTv3z8uvfTS2HTTTaNp06Zx/PHHx1dffVWuZRX77LPPIqUUzZs3L/Hav/TSS7nXvjzv21q1akXNmjXz2goLC2PRokUl5l1+Wyoe6Ke4z3/OvqtYWd8rxf+W9l4prW15n332WTz88MMl+m/DDTeMiMj14aGHHhqjR4+Ojz/+OPbee+9o1qxZbLXVVrltEwB+a1yzEQAqseIf9LNnzy4x7dNPP40qVapEw4YN89rnzJkTrVu3zt3/4YcfYv78+XnhwDbbbBPbbLNNLF26NCZNmhRXX311nHjiidG8efM44IADSq2ladOmERHx73//O9q0abPCmmvWrFnq9dLmzZuXd03CYis62qq09iZNmkTjxo3j8ccfL/UxdevWXWFdWalfv34MGjQobrrppvjzn/8cY8aMiYMOOigaNGiw0sf99LVcPvj59NNPS/TNZ599VmIZc+bMyVtWRfdH48aNV7htFtf3U6s6su6n+vfvH61atYoxY8ZE//79Y8yYMbHVVlvFBhtskJvn7rvvjurVq8cjjzySF5I99NBDpS6zrM9f1vUqfs7lt/fSjnxr165dbiCl6dOnx7333hvDhg2LJUuW5ILr8mjSpEkUFBTEc889V+qI3sVtP33frkk/Z99V1scW93/xfCt7r6xMkyZNolu3bjFixIhSpxeHyxE/Xkf08MMPj2+++SaeffbZOO+882K33XaL6dOnR7t27Vb5XADwa+LIRgCoxLp06RKtW7eOO++8M2903W+++Sbuv//+3CivP3XHHXfk3b/33nvjhx9+yBsJuljVqlVjq622yo14O3ny5BXWsuOOO0bVqlXjuuuuW2nN7du3jzfffDOvbfr06TFt2rSVPq4sdtttt5g/f34sXbo0Nt988xK3Ll26lHuZyx+RVRbHH398zJs3L/bZZ5/48ssv47jjjlvlY/7nf/4nIiJuv/32vPZXX3013n333dxo28W++uqrGDduXF7bnXfeGVWqVMkN5rI6+qM8tttuu5g6dWqJ7ebWW2+NgoKC6Nev389edtWqVePQQw+Nhx56KJ577rmYNGlSiaNHCwoKolq1anmn83733Xdx2223/eznjSj7ehWPdrz89r7867a8zp07x9lnnx0bb7zxSt9zESvePnfbbbdIKcV//vOfUl/7jTfeOCIievXqFfXr14/rr7++xAjdq9PP2XcV69mzZxQVFZV4r/z73/+Op59+Ovde6dKlS7Ro0SLuvffevPk++eSTeOGFF1ZZ42677RZvv/12dOzYsdQ+/GnYWKx27dqx8847x1lnnRVLliyJd955Z5XPAwC/No5sBIBKqqCgIKpUqRKXXnppHHzwwbHbbrvFkCFDYvHixXHZZZfFl19+GRdffHGJxz3wwANRrVq12GGHHXKjUXfv3j13XbPrr78+nn766dh1112jbdu2sWjRohg9enRERN4Iy8tr3759nHnmmXHBBRfEd999FwceeGDUr18/pk6dGvPmzYvhw4dHxI+nHB5yyCFxzDHHxN577x0ff/xxXHrppbkjrH6JAw44IO64447YZZdd4oQTTogtt9wyqlevHv/+97/jmWeeiYEDB8aee+5ZrmVutNFGEfHjqLZ169aNmjVrRocOHUo95bhY586dY6eddorHHnssfve730X37t1X+TxdunSJP/zhD3H11VdHlSpVYuedd86NRt2mTZs46aST8uZv3LhxHH300fHJJ59E586dY/z48XHjjTfG0Ucfnbvu4uroj/I46aST4tZbb41dd901zj///GjXrl08+uijce2118bRRx9dpusjrswRRxwRl1xySRx00EFRVFQU+++/f970XXfdNa688so46KCD4g9/+EPMnz8/Lr/88lKP9CuPsq5XixYtYvvtt4+RI0dGw4YNo127djFhwoR44IEH8pb35ptvxnHHHRf77rtvrLfeelGjRo14+umn480334zTTz99pbUUh4aXXHJJ7LzzzlG1atXo1q1b9O7dO/7whz/E4YcfHpMmTYptt902ateuHbNnz45//etfsfHGG8fRRx8dderUiSuuuCKOPPLI2H777eOoo46K5s2bxwcffBBvvPFGbmTzrP2cfVexBg0axDnnnBNnnnlmHHbYYXHggQfG/PnzY/jw4VGzZs0477zzcs8xfPjwGDJkSOyzzz5xxBFHxJdffhnDhw+Pli1b5l0rsjTnn39+PPnkk9GrV684/vjjo0uXLrFo0aKYOXNmjB8/Pq6//vpYZ5114qijjoqioqLo3bt3tGzZMubMmRMjR46M+vXrxxZbbJFpvwFApVCBg9MAAD/DX//61xQR6a233sq1PfTQQ2mrrbZKNWvWTLVr107bbbddev755/MeVzwa9WuvvZYGDBiQ6tSpk+rWrZsOPPDA9Nlnn+Xme/HFF9Oee+6Z2rVrlwoLC1Pjxo1Tnz590rhx48pU36233pq22GKLVLNmzVSnTp20ySab5EbdTSmlZcuWpUsvvTStu+66qWbNmmnzzTdPTz/99ApHo/773/9e4jkGDRqUateuXerzf//99+nyyy9P3bt3z9XQtWvXNGTIkPT+++/n5itt9OSUSo6KnVJKo0aNSh06dEhVq1bNG0V4+dGof2rs2LEpItLdd99dekeVYunSpemSSy5JnTt3TtWrV09NmjRJhxxySJo1a1aJGjfccMM0ceLEtPnmm6fCwsLUsmXLdOaZZ5YYiXl19EdpVvT4jz/+OB100EGpcePGqXr16qlLly7psssuyxuBuHgE48suu2yVz7O8Xr16pYhY4Sjoo0ePTl26dEmFhYVp3XXXTSNHjkw333xz3ujGK6u/eNryI6iXZb1SSmn27Nlpn332SY0aNUr169dPhxxySJo0aVLedvTZZ5+lwYMHp65du6batWunOnXqpG7duqWrrroqb0Tn0ixevDgdeeSRqWnTpqmgoKDEeo0ePTpttdVWqXbt2qmoqCh17NgxHXbYYWnSpEl5yxk/fnzq06dPql27dqpVq1baYIMN0iWXXJKbvqL3XPF+pdjKXstYbrTnlMq271p+NOpiN910U+rWrVuqUaNGql+/fho4cGBuhOifuuGGG1KnTp1SjRo1UufOndPo0aPTwIED0yabbLLK+v773/+m448/PnXo0CFVr149NWrUKG222WbprLPOSl9//XVKKaVbbrkl9evXLzVv3jzVqFEjtWrVKu23337pzTffLFELAPwWFKS0Bs+XAAB+sRNOOCGuueaa+PLLL9fINQj5eYpH1J05c2aZRlguj759+8a8efPi7bffznS58Fvw5ZdfRufOnWOPPfaIG264oaLLAYBfHadRA0Al8dprr8Wrr74ao0ePjt13313QuBZavHhxTJ48OV555ZV48MEH48orr8w8aATKbs6cOTFixIjo169fNG7cOD7++OO46qqr4quvvooTTjihossDgF8lYSMAVBL77LNP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AFRS5Q4bTzzxxLj55psj4segsU+fPrHppptGmzZtYuLEiVnXBwAAAABUEuUOG++7777o3r17REQ8/PDDMWPGjHjvvffixBNPjLPOOivzAgEAAACAyqHcYeO8efOiRYsWERExfvz42HfffaNz587x+9//Pt56663MCwQAAAAAKodyh43NmzePqVOnxtKlS+Pxxx+P7bffPiIivv3226hatWrmBQIAAAAAlUO18j7g8MMPj/322y9atmwZBQUFscMOO0RExMsvvxxdu3bNvEAAAAAAoHIod9g4bNiw2GijjWLWrFmx7777RmFhYUREVK1aNU4//fTMCwQAAAAAKodyh40REfvss0+JtkGDBv3iYgAAAACAyqvc12yMiJgwYULstttu0bFjx+jUqVPstttu8dRTT2VdGwAAAABQiZQ7bLzmmmtip512irp168YJJ5wQxx9/fNSrVy922WWXuOaaa1ZHjQAAAABAJVDu06hHjhwZV111VRx33HG5tuOPPz569+4dI0aMyGsHAAAAAH47yn1k48KFC2OnnXYq0b7jjjvGwoULMykKAAAAAKh8yh027r777vHggw+WaP/HP/4RAwYMyKQoAAAAAKDyKdNp1H/5y19y/19//fVjxIgRMXHixOjZs2dERLz00kvx/PPPx8knn7x6qgQAAAAA1nplChuvuuqqvPsNGzaMqVOnxtSpU3NtDRo0iNGjR8fZZ5+dbYUAAAAAQKVQprBxxowZq7sOAAAAAKCSK/c1G38qpRQppaxqAQAAAAAqsTId2bi8W2+9NS677LJ4//33IyKic+fOccopp8Shhx6aaXEAQOmuenJ6RZdQqZy0Q+eKLgEAAH4Tyh02XnnllXHOOefEcccdF717946UUjz//PPxxz/+MebNmxcnnXTS6qgTAAAAAFjLlTtsvPrqq+O6666Lww47LNc2cODA2HDDDWPYsGHCRgAAAAD4jSr3NRtnz54dvXr1KtHeq1evmD17diZFAQAAAACVT7nDxk6dOsW9995bov2ee+6J9dZbL5OiAAAAAIDKp9ynUQ8fPjz233//ePbZZ6N3795RUFAQ//rXv2LChAmlhpAAAAAAwG9DuY9s3HvvvePll1+OJk2axEMPPRQPPPBANGnSJF555ZXYc889V0eNAAAAAEAlUO4jGyMiNttss7j99tuzrgUAAAAAqMTKFDYuXLgw6tWrl/v/ytSqVSuqVftZGSYAAAAAUImV6TTqhg0bxty5cyMiokGDBtGwYcMV3mrWrBnrr79+PPPMM6u1cAAAAABg7VKmQxCffvrpaNSoUUTEKkPExYsXx0MPPRRHH310vPfee7+8QgAAAACgUihT2NinT59S/78iPXr0iFdeeeXnVwUAAAAAVDrlHo26LJo1axaTJk1aHYsGAAAAANZSqyVsBAAAAAB+e4SNAAAAAEAmyhQ2vvnmm7Fs2bLVXQsAAAAAUImVKWzcZJNNYt68eRERse6668b8+fNXa1EAAAAAQOVTprCxQYMGMWPGjIiImDlzpqMcAQAAAIASqpVlpr333jv69OkTLVu2jIKCgth8882jatWqpc770UcfZVogAAAAAFA5lClsvOGGG2KvvfaKDz74II4//vg46qijom7duqu7NgAAAACgEilT2BgRsdNOO0VExGuvvRYnnHCCsBEAAAAAyFPmsLHYmDFjcv//97//HQUFBdG6detMiwIAAAAAKp8yDRDzU8uWLYvzzz8/6tevH+3atYu2bdtGgwYN4oILLjBwDAAAAAD8hpX7yMazzjorbr755rj44oujd+/ekVKK559/PoYNGxaLFi2KESNGrI46AQAAAIC1XLnDxltuuSVuuumm2H333XNt3bt3j9atW8cxxxwjbAQAAACA36hyn0b9+eefR9euXUu0d+3aNT7//PNMigIAAAAAKp9yh43du3ePa665pkT7NddcE927d8+kKAAAAACg8in3adSXXnpp7LrrrvHUU09Fz549o6CgIF544YWYNWtWjB8/fnXUCAAAAABUAuU+srFPnz4xffr02HPPPePLL7+Mzz//PPbaa6+YNm1abLPNNqujRgAAAACgEij3kY0REa1atTIQDAAAAACQp9xHNgIAAAAAlEbYCAAAAABkQtgIAAAAAGSiXGFjSik+/vjj+O6771ZXPQAAAABAJVXusHG99daLf//736urHgAAAACgkipX2FilSpVYb731Yv78+aurHgAAAACgkir3NRsvvfTSOOWUU+Ltt99eHfUAAAAAAJVUtfI+4JBDDolvv/02unfvHjVq1IiioqK86Z9//nlmxQEAAAAAlUe5w8ZRo0athjIAAAAAgMqu3GHjoEGDVkcdAAAAAEAlV+5rNkZEfPjhh3H22WfHgQceGHPnzo2IiMcffzzeeeedTIsDAAAAACqPcoeN//znP2PjjTeOl19+OR544IH4+uuvIyLizTffjPPOOy/zAgEAAACAyqHcYePpp58eF154YTz55JNRo0aNXHu/fv3ixRdfzLQ4AAAAAKDyKHfY+NZbb8Wee+5Zor1p06Yxf/78TIoCAAAAACqfcoeNDRo0iNmzZ5dof/3116N169aZFPVT//nPf+KQQw6Jxo0bR61ataJHjx7x2muvZf48AAAAAMAvU+6w8aCDDorTTjst5syZEwUFBbFs2bJ4/vnn489//nMcdthhmRb3xRdfRO/evaN69erx2GOPxdSpU+OKK66IBg0aZPo8AAAAAMAvV628DxgxYkQMHjw4WrduHSml2GCDDWLp0qVx0EEHxdlnn51pcZdcckm0adMmxowZk2tr3759ps8BAAAAAGSj3Ec2Vq9ePe64446YPn163HvvvXH77bfHe++9F7fddltUrVo10+LGjRsXm2++eey7777RrFmz2GSTTeLGG29c6WMWL14cCxcuzLsBAAAAAKtfuY9sLNaxY8dYd911IyKioKAgs4J+6qOPPorrrrsu/vSnP8WZZ54Zr7zyShx//PFRWFi4wlO2R44cGcOHD18t9QAAXPXk9IouoVI5aYfOmS5P/5dP1v0PALAq5T6yMSLi5ptvjo022ihq1qwZNWvWjI022ihuuummrGuLZcuWxaabbhoXXXRRbLLJJjFkyJA46qij4rrrrlvhY84444xYsGBB7jZr1qzM6wIAAAAASir3kY3nnHNOXHXVVTF06NDo2bNnRES8+OKLcdJJJ8XMmTPjwgsvzKy4li1bxgYbbJDXtv7668f999+/wscUFhZGYWFhZjUAAAAAAGVT7rDxuuuuixtvvDEOPPDAXNvuu+8e3bp1i6FDh2YaNvbu3TumTZuW1zZ9+vRo165dZs8BAAAAAGSj3KdRL126NDbffPMS7Ztttln88MMPmRRV7KSTToqXXnopLrroovjggw/izjvvjBtuuCGOPfbYTJ8HAAAAAPjlyh02HnLIIaVeM/GGG26Igw8+OJOiim2xxRbx4IMPxl133RUbbbRRXHDBBTFq1KjMnwcAAAAA+OXKdBr1n/70p9z/CwoK4qabboonnngitt5664iIeOmll2LWrFkrHCH6l9htt91it912y3y5AAAAAEC2yhQ2vv7663n3N9ts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fywx7ZhjjomCgoIYPHhwmZe3dOnSGDlyZHTt2jWKioqiUaNGsfXWW8eYMWPy5ivr+6C8f6z4Ne7Pfunn5opUxB84y/r6vPDCC7HLLrtEw4YNo2bNmrHxxhvHFVdcEUuXLs2br6K+E2T9vllTirejgoKCqF27dqy33noxePDgeO211/LmmzhxYt68RUVFseGGG8YNN9xQQZVXPsJGMjVz5szYbLPN4umnn45LL7003nrrrXj88cejX79+ceyxx1Z0eb8a5e3nF198MXr37h0REf/6179y/2flfs72XFBQEDNnzizT8idOnBjt27fPrmBYg5566qk44IADYp999olXXnklXnvttRgxYkQsWbLkZy9zyZIlUbVq1WjRokVUq1Ytw2rXPjvttFPMnj07Pvroo7jwwgvj2muvjT//+c8VXdZv1t577x1vvPFG3HLLLTF9+vQYN25c9O3bNz7//POKLu1X56OPPorNN988pk+fHnfddVd88MEHcf3118eECROiZ8+eK+zzX7Jv+bWo6JDi9ddfj9122y2aNWsWNWvWjPbt28f+++8f8+bNy2L1KlSbNm3i7rvvju+++y7XtmjRorjrrruibdu25VrWsGHDYtSoUXHBBRfE1KlT45lnnomjjjoqvvjii9w8P/d9UBarY3/2/fff/+zHZrXstf1zs6z7qLK8Pg8++GD06dMn1llnnXjmmWfivffeixNOOCFGjBgRBxxwQKSUVtdqlEuW75s1acyYMTF79ux455134q9//Wt8/fXXsdVWW8Wtt95aYt5p06bF7NmzY+rUqTFkyJA4+uijHXRSVgkytPPOO6fWrVunr7/+usS0L774Ys0X9CtV3n7eaqut0oMPPphSSmm33XZL11133Wqu8Nfh52zPEZFmzJhRpuU/88wzqV27dj+/wN+AQYMGpYEDB6aUUnrsscdS7969U/369VOjRo3Srrvumj744IPcvFtvvXU67bTT8h4/d+7cVK1atfT000+nlFK67bbb0mabbZbq1KmTmjdvng488MD02WefrbH1WZ3WdF+dcMIJqW/fvqus6x//+EfabLPNUmFhYWrcuHHac889c9PatWuXLrjggjRo0KBUr169dNhhh6UZM2akiEivv/56SunH90lEpEceeSR169YtFRYWpi233DK9+eabedN/ejvvvPN+TheuMT99rYodeeSRqUWLFqljx47psssuy5v21ltvpYKCgvTBBx+kdu3a5a1r8T7kvPPOS927d0+33nprateuXapXr17af//908KFC3PLWbRoURo6dGhq2rRpKiwsTL17906vvPJKbnpxXz711FNps802S0VFRalnz57pvffeW219sTb44osvUkSkiRMnrnSeo446KjVr1iwVFhamDTfcMD388MMppZTmzZuXDjjggNS6detUVFSUNtpoo3TnnXfmPb5Pnz7phBNOyN3/Ne+LVmWnnXZK66yzTvr222/z2mfPnp1q1aqV/vjHP6aUSt8/pJTSqaeemtZbb71UVFSUOnTokM4+++y0ZMmSvGWtar9z1VVX5e5/+eWX6aijjkpNmzZNdevWTf369UtTpkxZTWv/y/zud79LW221VXr66afTzJkz08svv5wuuuii9Mgjj+TmeeCBB1K1atXSUUcdlV5//fU0Y8aMdOONN6aGDRumffbZJy1btiw3b0Tkvh+uymeffZYaNWqUBg0alCZPnpw++uijNGHChHTCCSekjz/++Gev0+LFi3/2Y1dm2bJl6fvvvy/TvMX75I033jjdfvvtufY77rgjbbzxxmngwIFp0KBBKaWUbrnlltSoUaO0aNGivGXstdde6dBDD00ppdS9e/c0bNiwlT5nWd8HKZXcf6xMWfZnKa16uy/+TLn55ptThw4dUkFBQbr++utTq1at0tKlS/OWNWDAgNz7M6WUxo0blzbddNNUWFiYOnTokIYNG5b3WkREuu6669Luu++eatWqlc4999xVrtfKPjdX9dn2+eefp4MOOig1adIk1axZM3Xq1CmNHj06V8tPb3369EkppfT999+noUOH5r5HnXrqqemwww7Lq6FPnz7p2GOPTSeddFJq3Lhx2nbbbVNKKb3zzjtp5513TrVr107NmjVLhxxySPrvf/+bUirb6/P111+nxo0bp7322qvEtHHjxqWISHfffXdef5b1fZyl8rxvsvr+ccEFF6SmTZumOnXqpN///vfptNNOS927d89NX7p0aRo+fHhq3bp1qlGjRurevXt67LHH8paxov467LDDUt26ddPnn3+eV9Pyv/nWXXfddOmll/6MHvvtETaSmfnz56eCgoJ00UUXVXQpv2pl7ec77rgj1a9fP9WvXz8VFBSkOnXqpPr166cqVaqk2rVrp/r166c77rhjDVVd+fzc7VnYmK2ffrm877770v3335+mT5+eXn/99TRgwIC08cYb5770Xn311alt27Z5P6Suvvrq1Lp169w8N998cxo/fnz68MMP04svvpi23nrrtPPOO6/x9Vod1nRfjRw5MjVt2jS99dZbK6zpkUceSVWrVk3nnntumjp1apoyZUoaMWJEbnpxKHbZZZel999/P73//vsrDBvXX3/99MQTT6Q333wz7bbbbql9+/ZpyZIlafHixWnUqFGpXr16afbs2Wn27Nnpq6++yqpbV4vSfjQNHTo0NW7cOI0YMSJtsMEGedNOOumk3I+YuXPnpohIY8aMSbNnz05z585NKf34w7BOnTppr732Sm+99VZ69tlnU4sWLdKZZ56ZW87xxx+fWrVqlcaPH5/eeeedNGjQoNSwYcM0f/78lNL/9fVWW22VJk6cmN555520zTbbpF69eq3G3qh433//fapTp0468cQTSwQIKf3442XrrbdOG264YXriiSfShx9+mB5++OE0fvz4lFJK//73v9Nll12WXn/99fThhx+mv/zlL6lq1arppZdeyi1j+bDg17wvWplVfbYeddRRqWHDhmnZsmWl7h9S+vHH5vPPP59mzJiRxo0bl5o3b54uueSS3DLKst8pDhuXLVuWevfunQYMGJBeffXVNH369HTyySenxo0b594Xa4uKDikefPDBVK1atVUGeCsLWlIqPaA54IAD0v7775+3nCVLlqTGjRvnQqFly5alSy65JHXo0CHVrFkzdevWLf3973/PzV+8/3r88cfTZpttlqpXr57749mqFO+Tr7zyyrTddtvl2rfbbrt01VVX5YUm3377bapfv3669957c/P997//TTVq1Mg9X//+/dO2226b2z8vrzzvg+I+K2vYuKr9WUpl2+7PO++8VLt27dS/f/80efLk9MYbb6R58+alGjVqpKeeeiq3rM8//zzVqFEj/e///m9KKaXHH3881atXL40dOzZ9+OGH6Yknnkjt27fPC18jIjVr1izdfPPN6cMPP0wzZ85c5Xqt7HNzVZ9txx57bOrRo0d69dVX04wZM9KTTz6Zxo0bl1JK6ZVXXsmFXLNnz8495sILL0yNGjVKDzzwQHr33XfTH//4x1SvXr0SYWOdOnXSKaeckt5777307rvvpk8//TQ1adIknXHGGendd99NkydPTjvssEPq169fmV+fBx54IEVEeuGFF0qd3rlz57w6KjpsLMv7JovvH7fffnuqWbNmGj16dJo2bVoaPnx4qlevXl7YeOWVV6Z69eqlu+66K7333nvp1FNPTdWrV0/Tp0/PzbOi/nr99ddTRKR77rknr6bisHHZsmXpscceS9WrV0///Oc/M+rFXzdhI5l5+eWXU0SkBx54oKJL+VUraz9/9dVXub9mb7jhhmnGjBnpH//4R2rZsmWaMWNGmjFjxlr/g7wi/dztWdiYrdK+XBYrDl2Kw67iI/OeffbZ3Dw9e/ZMp5xyygqXX/wl89fwXljTffX111+nXXbZJXd03f77759uvvnmvC/PPXv2TAcffPAKl9muXbu0xx575LWtKGz86Q/k+fPnp6KiotwXwjFjxqT69euv8HnWNsu/Vi+//HJq3Lhx2m+//dKnn36aqlatml5++eWU0o8/uJs2bZrGjh2bm7+0L8rnnXdeqlWrVt6RjKecckraaqutUko/vl7Vq1fP+yPTkiVLUqtWrXJ/of/pkQXFHn300RQR6bvvvsts/ddG9913X2rYsGGqWbNm6tWrVzrjjDPSG2+8kVJK6X//939TlSpV0rRp08q8vF122SWdfPLJufurCgt+TfuilXnppZdW+sP4yiuvTBGRPvvss1L3D6W59NJL02abbZa7X5b9TnHYOGHChFSvXr0SP/o7duyY/va3v616hdagig4pXnzxxRQR6d577837Q9VPrSpoSan0gObhhx9ORUVFedv/ww8/nGrWrJkWLFiQUkrpzDPPTF27dk2PP/54+vDDD9OYMWNSYWFhLnwt3n9169YtPfHEE+mDDz5I8+bNK9O6Fe+T//vf/6bCwsI0Y8aMNHPmzFSzZs303//+Ny80SSmlo48+Ou+PA6NGjUrrrrturl/eeeedtP7666cqVaqkjTfeOA0ZMiT3x4mUyvc+KO6zsoaNKa18f5ZS2bb78847L1WvXr1EYLr77runI444Inf/b3/7W2rRokX64YcfUkopbbPNNiVC1Ntuuy21bNkydz8i0oknnljm9UlpxZ+b++yzzyo/2wYMGJAOP/zwUpe7/HeOYs2bN887y+CHH35Ibdu2LRE29ujRI+9x55xzTtpxxx3z2mbNmpUiIvcZsqrX5+KLLy71iLpiu+++e1p//fVz9ys6bFzV+yar7x9bbbVVOvbYY/Nq6N27d17Y2KpVq7w/LqWU0hZbbJGOOeaY3P0V9dd3332XIiL3x6vimmrXrp1q166dqlWrlqpUqZIuvPDCn9dhv0Gu2Uhm0v9/7YiCgoIKruTXraz9XKdOnWjfvn1Mnjw5Bg4cGO3bt4+33nordtlll2jfvn20b98+6tSpsyZKrpTK2s8777xz1KlTJ3eLiNhwww1LtBX7afvOO+8cn3zySYk2Svfhhx/GQQcdFOuuu27Uq1cvOnToEBERn3zySURENG3aNHbYYYe44447IiJixowZ8eKLL8bBBx+cW8brr78eAwcOjHbt2kXdunWjb9++ecv4tVgTfVW7du149NFH44MPPoizzz476tSpEyeffHJsueWW8e2330ZExJQpU2K77bZbaa2bb755mdapZ8+euf83atQounTpEu+++26ZHrs2euSRR6JOnTpRs2bN6NmzZ2y77bZx9dVXR8uWLWPXXXeN0aNH5+ZbtGhR7LvvvqtcZvv27aNu3bq5+y1btoy5c+dGxI/bxPfff593zd7q1avHlltuWaIfu3XrlreMiMgt59dq7733jk8//TTGjRsX/fv3j4kTJ8amm24aY8eOjSlTpsQ666wTnTt3LvWxS5cujREjRkS3bt2icePGUadOnXjiiSdWul/5reyLymv5z97S9g/33Xdf/O53v4sWLVpEnTp14pxzzsnrt7Lsd4q99tpr8fXXX+det+LbjBkz4sMPP8xgjbJTrVq1GDt2bNxyyy3RoEGD6N27d5x55pnx5ptv5uaZPn16RESsv/76pS6ja9euuXnKa+utt44zzzwzDjrooGjSpEnsvPPOcdlll8Vnn32Wm+e6666LTTfdNC666KLo2rVrbLLJJjF69Oh45pln8p63U6dOcemll0aXLl2ia9eu0b9//6hdu3Y8+OCDuXnuvPPOGDBgQNSrVy+++eabuPLKK2P06NHRv3//WHfddWPw4MFxyCGHxN/+9re8Os8///zYYYcdomPHjtG4ceNyrWOTJk1i1113jVtuuSXGjBkTu+66azRp0qTEfEcddVQ88cQT8Z///Ccifrz+W/FgGRERG2ywQbz99tvx0ksvxeGHHx6fffZZDBgwII488sgy1VH8PqhRo0a56i+2sv1ZRNm3+3bt2kXTpk3zln3wwQfH/fffH4sXL46IiDvuuCMOOOCAqFq1am7Z559/ft5yjzrqqJg9e3buu0FE2T/7f6q0z82hQ4eu8rPt6KOPjrvvvjt69OgRp556arzwwgsrfZ4FCxbEZ599FltuuWWurWrVqrHZZpuVmHf59XjttdfimWeeyVv/rl27RkTk+nZVr0+x4u1geSmln71trA6ret9k9f1j2rRpea9JROTdX7hwYXz66aclxibo3bt3mb4vrui333PPPRdTpkyJKVOmxE033RQXXXRRXHfddatcHgaIIUPrrbdeFBQUVOoff5VBWfr5pwHWDTfcEFdccUXUqVMnhg0bFrfddlvUqVOn1JHD+D9l3Z5vuumm3AdQ8Uh248ePL9FW7KftN910U7Rq1apEG6UbMGBAzJ8/P2688cZ4+eWX4+WXX46I/AtyH3zwwXHffffF999/H3feeWdsuOGG0b1794iI+Oabb2LHHXeMOnXqxO233x6vvvpq7ofNr23ggTXZVx07dowjjzwybrrpppg8eXJMnTo17rnnnoiIKCoqWmWttWvX/tnrWZn/uNWvX7+YMmVKTJs2LRYtWhQPPPBANGvWLCIijjzyyNwF18eMGRP7779/1KpVa5XLrF69et79goKCWLZsWUSs+Et0SqlE20+XUzyteDm/ZjVr1owddtghzj333HjhhRdi8ODBcd55561yO77iiiviqquuilNPPTWefvrpmDJlSvTv33+F+5Xf0r5oeZ06dYqCgoKYOnVqqdPfe++9aNiwYe6H6vL7h5deeikOOOCA2HnnneORRx6J119/Pc4666y8fivLfqfYsmXLomXLlnmfw8Xvy1NOOeVnrOHqVdEhxYgRI2LOnDlx/fXXxwYbbBDXX399dO3aNd56662IKFvQElEyoKlevXrsu+++uT+AffPNN/GPf/wj9wewqVOnxqJFi2KHHXbIW/att95aIhT+OSHWTx1xxBG5UPeII44odZ5NNtkkunfvHrfeemtMnjw53nrrrRKj7lapUiW22GKLOOmkk+LBBx+MsWPHxs033xwzZswo0/ugadOm0aBBg5+9Hivan0WUfbsv7fN5wIABsWzZsnj00Udj1qxZ8dxzz8UhhxySm75s2bIYPnx43nLfeuuteP/996NmzZorXfaqlPa5Wb9+/YhY+WfbzjvvHB9//HGceOKJ8emnn8Z2221XpoFlSlvm8pZfj2XLlsWAAQNK9O37778f2267bW6+lb0+6623XkTECn+DvPfeeyv841dFWdn7JsvvH2V5TcryPKUp7u/iP9AX69ChQ3Tq1Ck23HDDOPzww+PQQw+NESNGrHJ5CBvJUKNGjaJ///7x17/+Nb755psS07/88ss1X9SvUFn6uTjA+t///d+oVq1aTJkyJRc2FP915vzzz1/TpVcqZd2eW7duHZ06dcrdIn78S/DybcV+2t66deuoVq1aiTZKmj9/frz77rtx9tlnx3bbbRfrr79+3qiOxfbYY49YtGhRPP7443HnnXfmfQF+7733Yt68eXHxxRfHNttsE127dv1VHq1VkX3Vvn37qFWrVu49061bt8xG7HvppZdy///iiy9i+vTpuR+xNWrUKDHK6tqudu3a0alTp2jXrl2JkHCXXXaJ2rVrx3XXXRePPfZYiS/u1atXL/f6durUKWrUqBH/+te/cm3ff/99TJo0aYVHQf3WbbDBBvHNN99Et27d4t///vcKjwh77rnnYuDAgXHIIYdE9+7dY9111433339/hcv9reyLStO4cePYYYcd4tprr80bvTQiYs6cOXHHHXfE/vvvv8Ifhs8//3y0a9cuzjrrrNh8881jvfXWi48//jhvnvLsdzbddNOYM2dOic/iTp06lXpE29qgokOKxo0bx7777htXXHFFvPvuu9GqVau4/PLLI6LsQUtpQdPBBx8cTz31VMydOzceeuihqFmzZu5sj+Kw4dFHH81b7tSpU+O+++7LW84v+QNWxI8jHi9ZsiSWLFkS/fv3X+F8Rx55ZIwZMyZGjx4d22+/fbRp02aly91ggw0i4scgtSzvg+XDy1+qeH8W8cu2+6Kiothrr73ijjvuiLvuuis6d+6cd8TfpptuGtOmTSux3E6dOkWVKr8seijtc7Osn21NmzaNwYMHx+233x6jRo2KG264ISL+7+jRn36m1q9fP5o3bx6vvPJKrm3p0qXx+uuvr7LGTTfdNN55551o3759ifVf2bb509enf//+0ahRo7jiiitKzDdu3Lh4//33M98+fqmVvW+y+v7RpUuXvNckImLSpEm5/9erVy9atWqV9zwRES+88EKZnmfUqFFRr1692H777Vc6X9WqVUu8byldtYougF+Xa6+9Nnr16hVbbrllnH/++dGtW7f44Ycf4sknn4zrrrvOUY8ZKUs/d+rUKSZNmhRbbbVVdO3aNZ599tlYd911Sxx+zorZntceDRs2jMaNG8cNN9wQLVu2jE8++SROP/30EvPVrl07Bg4cGOecc068++67cdBBB+WmtW3bNmrUqBFXX311/PGPf4y33347LrjggjW5GmvEmuqrYcOGxbfffhu77LJLtGvXLr788sv4y1/+Et9//33ssMMOERFx3nnnxXbbbRcdO3aMAw44IH744Yd47LHH4tRTTy33ep1//vnRuHHjaN68eZx11lnRpEmT2GOPPSLix5Dz66+/jgkTJkT37t2jVq1aZToScG1VtWrVGDx4cJxxxhnRqVOnvFPII35c3wkTJkTv3r2jsLAwGjZsuMpl1q5dO44++ug45ZRTolGjRtG2bdu49NJL49tvv43f//73q2tVKoX58+fHvvvuG0cccUR069Yt6tatG5MmTYpLL700Bg4cGH369Iltt9029t5777jyyiujU6dO8d5770VBQUHstNNO0alTp7j//vvjhRdeiIYNG8aVV14Zc+bMWeGPm9/KvmhFrrnmmujVq1f0798/LrzwwujQoUO88847ccopp0Tr1q1XesRIp06d4pNPPom77747tthii3j00UfzTr2NKN9+Z/vtt4+ePXvGHnvsEZdcckl06dIlPv300xg/fnzssccev/gouTVhgw02iIceeigi8kOKXr165c1XHFKMGjUqs+euUaNGdOzYMS/Euv/++6N9+/ZRrVr5fmb26tUr2rRpE/fcc0889thjse++++aCoA022CAKCwvjk08+iT59+mRWf2mqVq2a+35XfGpwaQ4++OD485//HDfeeGPceuutedP22Wef6N27d/Tq1StatGgRM2bMiDPOOCM6d+6c+yPZyt4HnTt3jnPPPTdvmf/9739LnC3TokWLaNGiRV7bqvZnEb98uz/44INjwIAB8c477+T9oTIi4txzz43ddtst2rRpE/vuu29UqVIl3nzzzXjrrbfiwgsvXOlyf46yfLade+65sdlmm8WGG24YixcvjkceeSS3f27WrFkUFRXF448/Huuss07UrFkz6tevH0OHDo2RI0dGp06domvXrnH11VfHF198scoj5I499ti48cYb48ADD4xTTjklmjRpEh988EHcfffdceONN8aXX365ytendu3a8be//S0OOOCA+MMf/hDHHXdc1KtXLyZMmBCnnHJKHHnkkbHLLrvkPe+MGTNKbB+dOnVaY5fMWtn7JqvvH0OHDo2jjjoqNt988+jVq1fcc8898eabb8a6666bm+eUU06J8847Lzp27Bg9evSIMWPGxJQpU3JHTRf78ssvY86cObF48eKYPn16/O1vf4uHHnoobr311hJHFM+dOzcWLVoUixcvjldeeSVuu+222GeffcrZQ79Ra/oikfz6ffrpp+nYY49N7dq1SzVq1EitW7dOu+++e3rmmWcqurRflbL085AhQ9LZZ5+dUkrp/PPPT0ceeWQFVVt5lXd7DgPEZOrQQw9Ne++9d0oppSeffDKtv/76qbCwMHXr1i1NnDix1Is8F19Qunj03p+68847U/v27VNhYWHq2bNnbnTO5S8MXhmt6b56+umn0957753atGmTatSokZo3b5522mmn9Nxzz+Ut5/777089evRINWrUSE2aNMkbJfWnAzUUW9EAMQ8//HDacMMNU40aNdIWW2yRpkyZkve4P/7xj6lx48YpItJ5551X/g5cg1Y2mE+xDz/8MEVE7uLpPzVu3LjUqVOnVK1atdw+5Lzzzsu7SHpKKV111VV5+5jvvvsuDR06NDVp0iQVFham3r17p1deeSU3ffmRF1P6v9EZy7pfq4wWLVqUTj/99LTpppum+vXrp1q1aqUuXbqks88+O3377bcppR8HJTr88MNT48aNU82aNdNGG22UHnnkkdy0gQMHpjp16qRmzZqls88+Ox122GElBhL46QAPv+Z9UVnMnDkzDR48OLVo0SJVr149tWnTJg0dOjRvQI/S9g8p/TjwUePGjVOdOnXS/vvvn6666qoSA0SVZ7+zcOHCNHTo0NSqVatcLQcffHD65JNPsl7tX2TevHmpX79+6bbbbktvvPFG+uijj9K9996bmjdvnjdgx9///vdUtWrVdNRRR6U33ngjzZgxI910002pYcOGJb4HRkS68sor0+uvv553K22goocffjgdfPDB6eGHH07Tpk1L7733XrrssstS1apV06233ppSSuk///lPatq0adpnn33Syy+/nD788MP0v//7v+nwww/PDSCyssFOzjzzzLTBBhukatWqlfgsOeuss1Ljxo3T2LFj0wcffJAmT56crrnmmtzgWaXtv8pqVfvk5QeIKXbooYemRo0alRho5YYbbkj9+vVLTZs2TTVq1Eht27ZNgwcPLjHq8owZM9KgQYNS8+bNU0FBQYqItNdee6Vvvvkmb74+ffqkiChxK+2zriz7s5RWvd2X9plS7IcffkgtW7ZMEZE+/PDDEtMff/zx1KtXr1RUVJTq1auXttxyy3TDDTfkppf2fWRVVvYareqz7YILLkjrr79+KioqSo0aNUoDBw5MH330UW76jTfemNq0aZOqVKmS+vTpk1L6cUCm4447LtWrVy81bNgwnXbaaWnfffdNBxxwQO5xK9qWp0+fnvbcc8/UoEGDVFRUlLp27ZpOPPHEtGzZsjK/Piml9Oyzz6b+/funevXq5V7ziy++uMTzlbZtRMRq/+1dnvdNVt8/zj///NSkSZNUp06ddMQRR6Tjjz8+bb311rnpS5cuTcOHD0+tW7dO1atXT927d0+PPfZYXl0/7aOaNWumjh07pkGDBqXXXnstb77imopv1apVSx06dEh//vOf09dff13+DvsNEjYCsNbq379/iZHnKN2vta9+yQ/Iyuxf//pXqlatWpozZ05FlwKsBSo6pPjwww/TUUcdlTp37pyKiopSgwYN0hZbbJHGjBmTN9/KgpaUVh42vvPOOykiUrt27UqMeL1s2bL0//7f/0tdunRJ1atXT02bNk39+/dP//znP1NKFfNZsf3226ehQ4dmtrxzzz031alTZ4WjiVNxli5dmjp37pw7iGNN++6779KOO+6Y1l9//RIjhP+Wbb/99umQQw6p6DJYgYKUVnAFYQCoIF988UW88MILsffee8fdd9+dO12Wkn7tfTVx4sTo169ffPHFF7/oYvmVxeLFi2PWrFnxhz/8IVq2bFni1B+A8li0aFEMHDgwZs2aFf/85z9LjC5M+X3++efxxBNPxMEHHxxTp06NLl26ZLbsMWPGxIIFC+L444//xdc45Of7+OOP44knnog+ffrE4sWL45prrokxY8bEG2+8UWHXOV60aFGMGjUq1ltvvdh7770rpIaK9O2338b1118f/fv3j6pVq8Zdd90V559/fjz55JOrvM4iFUPYCMBaZ88994xXX301Bg0aFBdeeGGlHnV4dfu199VvLWwcO3Zs/P73v48ePXrEuHHjDBoF/GK/9ZAia+3bt48vvvgizjnnnDKNakzlM2vWrDjggAPi7bffjpRSbLTRRnHxxRfnDXTEmvXdd9/FgAEDYvLkybF48eLo0qVLnH322bHXXntVdGmsgLARAAAAAMiEY7MBAAAAgEwIGwEAAACATAgbAQAAAIBMCBsBAAAAgEwIGwEAAACATAgbAQCIiIi+ffvGiSeeWNFlAABQiQkbAQAAAIBMCBsBAAAAgEwIGwEAKOH222+PzTffPOrWrRstWrSIgw46KObOnZubPnHixCgoKIgJEybE5ptvHrVq1YpevXrFtGnT8pZz4YUXRrNmzaJu3bpx5JFHxumnnx49evTITS/t1O099tgjBg8eXOZaIiLGjRsX6623XhQVFUW/fv3illtuiYKCgvjyyy9z87zwwgux7bbbRlFRUbRp0yaOP/74+Oabb35xXwEA8H+EjQAAlLBkyZK44IIL4o033oiHHnooZsyYkRcAFjvrrLPiiiuuiEmTJkW1atXiiCOOyE274447YsSIEXHJJZfEa6+9Fm3bto3rrrsu81pmzpwZ++yzT+yxxx4xZcqUGDJkSJx11ll5y3jrrbeif//+sddee8Wbb74Z99xzT/zrX/+K4447rtz1AACwYgUppVTRRQAAUPH69u0bPXr0iFGjRpWY9uqrr8aWW24ZX331VdSpUycmTpwY/fr1i6eeeiq22267iIgYP3587LrrrvHdd99FzZo1Y+utt47NN988rrnmmtxyfve738XXX38dU6ZMWeFz7rHHHtGgQYMYO3ZsqXUuX8vpp58ejz76aLz11lu5ec4+++wYMWJEfPHFF9GgQYM47LDDoqioKP72t7/l5vnXv/4Vffr0iW+++SZq1qz58zsOAIAcRzYCAFDC66+/HgMHDox27dpF3bp1o2/fvhER8cknn+TN161bt9z/W7ZsGRGRO8V52rRpseWWW+bNv/z9LGqZNm1abLHFFit9ntdeey3Gjh0bderUyd369+8fy5YtixkzZpS7JgAASletogsAAGDt8s0338SOO+4YO+64Y9x+++3RtGnT+OSTT6J///6xZMmSvHmrV6+e+39BQUFERCxbtqxEW7HlT6qpUqVKibbvv/++XLWklFb5PMuWLYshQ4bE8ccfX2J927ZtW3pHAABQbsJGAADyvPfeezFv3ry4+OKLo02bNhERMWnSpHIvp0uXLvHKK6/EoYcemmtbfjlNmzaN2bNn5+4vXbo03n777ejXr1+Za+natWuMHz8+r235eTbddNN45513olOnTuVeDwAAys5p1AAA5Gnbtm3UqFEjrr766vjoo49i3LhxccEFF5R7OUOHDo2bb745brnllnj//ffjwgsvjDfffDPvKMT/+Z//iUcffTQeffTReO+99+KYY47JG0G6LLUMGTIk3nvvvTjttNNi+vTpce+99+au91j8XKeddlq8+OKLceyxx8aUKVPi/fffj3HjxsXQoUPL30EAAKyQsBEAgDxNmzaNsWPHxt///vfYYIMN4uKLL47LL7+83Ms5+OCD44wzzog///nPsemmm+ZGkf7pYCxHHHFEDBo0KA477LDo06dPdOjQIXdUY1lr6dChQ9x3333xwAMPRLdu3eK6667LjUZdWFgYET9eW/Kf//xnvP/++7HNNtvEJptsEuecc07uOpMAAGTDaNQAAKwxO+ywQ7Ro0SJuu+221fo8I0aMiOuvvz5mzZq1Wp8HAIB8rtkIAMBq8e2338b1118f/fv3j6pVq8Zdd90VTz31VDz55JOZP9e1114bW2yxRTRu3Dief/75uOyyy+K4447L/HkAAFg5YSMAAKtFQUFBjB8/Pi688MJYvHhxdOnSJe6///7YfvvtM3+u4mtCfv7559G2bds4+eST44wzzsj8eQAAWDmnUQMAAAAAmTBADAAAAACQCWEjAAAAAJAJYSMAAAAAkAlhIwAAAACQCWEjAAAAAJAJYSMAAAAAkAlhIwAAAACQCWEjAAAAAJCJ/w+9j5L13GSjfgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1600x800 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_excel ('github-New-job-posting.xlsx')\n",
    "print (df)\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "\n",
    "postings = [12,10,10,10,7,6,6,5,4,3,2,1]\n",
    "df = [\"C\",\"C#\",\"C++\",\"Java\",\"JavaScript\",\"Python\",\"Scala\",\"Oracle\",\"SQL Server\",\"MySQL Server\",\"PostgreSQL\",\"MongoDB\"]\n",
    "hs = np.arange(len(df))\n",
    "plt.figure(figsize=(16,8))\n",
    "plt.bar(hs, postings, align='center', alpha=0.5)\n",
    "plt.xlabel(\"language\")\n",
    "plt.ylabel(\"number of jobs\")\n",
    "plt.xticks(hs, df)\n",
    "plt.title('Jobs currently open for various technologies')\n",
    "\n",
    "plt.show"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Authors\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Ayushi Jain\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Other Contributors\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Rav Ahuja\n",
    "\n",
    "Lakshmi Holla\n",
    "\n",
    "Malika\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer\\&utm_source=Exinfluencer\\&utm_content=000026UJ\\&utm_term=10006555\\&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2021-01-01\\&cm_mmc=Email_Newsletter-\\_-Developer_Ed%2BTech-\\_-WW_WW-\\_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264\\&cm_mmca1=000026UJ\\&cm_mmca2=10006555\\&cm_mmca3=M12345678\\&cvosrc=email.Newsletter.M12345678\\&cvo_campaign=000026UJ).\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<!--## Change Log\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<!--| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |\n",
    "| ----------------- | ------- | ----------------- | ---------------------------------- | \n",
    "| 2022-01-19        | 0.3     | Lakshmi Holla        | Added changes in the markdown      |\n",
    "| 2021-06-25        | 0.2     | Malika            | Updated GitHub job json link       |\n",
    "| 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |--!>\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python",
   "language": "python",
   "name": "conda-env-python-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  },
  "prev_pub_hash": "c4d9a957e70e09027735f73df3308c8386dea312a4960cb2534d8e6ade9a49cc"
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
