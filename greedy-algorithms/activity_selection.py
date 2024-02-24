from job import Job
import job_examples
import quick_sort

def compare_by_endtime(job1, job2):
    return job1.end <= job2.end
    
def activity_selection(jobs):
    quick_sort.call_quick_sort(jobs, compare_by_endtime)
    print('After sort by endtime:')
    print_jobs(jobs[1:])
    A = []
    e = 0
    for job in jobs[1:]:
        if job.start >= e:
            A.append(job)
            e = job.end
            print(f'Selected {job}')
            print(f'New endtime {e}')
        else:
            print(f'job {job.name} start {job.start} is before endtime {e}')
    return A

def print_jobs(jobs):
    print('Activities selected:')
    for job in jobs: print(job)