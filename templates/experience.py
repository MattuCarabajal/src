from flask import Markup
from libs.csv import csv_to_list_dict


def get_jobs():
    jobs = csv_to_list_dict( 'data_vault/jobs.csv' )
    jobs_descriptions_list = csv_to_list_dict( 'data_vault/jobs_descriptions.csv' )

    jobs_descriptions = {}
    for job_project_descriptions in jobs_descriptions_list:
        jobs_descriptions_aux = {}
        company = job_project_descriptions[ 'company_name' ]
        project = job_project_descriptions[ 'project_name' ]
        description = job_project_descriptions[ 'description' ]
        if company not in jobs_descriptions:
            jobs_descriptions[ company ] = { project : description }
        else:
            jobs_descriptions[ company ][ project ] = description
            

    jobs_complete = []
    for job in jobs:
        job_complete = {
            'name': job[ 'name' ],
            'url': job[ 'url' ],
            'img_src': job[ 'img_src' ],
            'time_span' : job[ 'time_span' ],
            'position' : job[ 'position' ],
            'city' : job[ 'city' ]
        }
        
        projects = []
        job_projects = job[ 'projects_names' ].split( ',' )
        for project in job_projects:
            project = {
                    'name' : project,
                    'description' : Markup( f"{ jobs_descriptions[ job[ 'name' ] ][ project ] }<br>" )
            }
            projects.append( project )
            job_complete[ 'projects' ] = projects
        
        jobs_complete.append( job_complete )
    return jobs_complete

if __name__ == '__main__':
    print( get_jobs() )