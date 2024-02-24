from job import Job
import job_examples
import quick_sort
import min_priority_queue

# entry for min-PQ. We need to keep track of both job and machine.
# We need to know which machine the job was on, when we
# take it out of the queue.
# We also need both >= and < operators for the heap implementation
# I think we could avoid the '<' in the heap, but..
class PQ_Entry: 
    def __init__(self, job, machine):
        self.job = job
        self.machine = machine

    def __ge__(self, other):
        return self.job.end  >= other.job.end

    #def __lt__(self, other):
     #   return not (self >= other)

def print_jobs(jobs):
    for j in jobs[1:]: print(j)

def schedule(jobs):
    S = [None] # there is no machine 0 here.
    m = 0
    end_times = min_priority_queue.min_priority_queue([None])
    quick_sort.call_quick_sort(jobs)
    print('After sorting by start time:')
    print_jobs(jobs)
    
    for job in jobs[1:]:
        print(f'Schedule next job {job}')
        scheduled = False
        if m > 0:
            earliest_job_to_end = end_times.minimum()
            earliest_end = earliest_job_to_end.job.end
            job_m = earliest_job_to_end.machine
            print(f'Earliest end time: machine {job_m} time {earliest_end}')
            if job.start >= earliest_end:
                # schedule it on that machine
                print(f'Schedule job on: machine {job_m}')
                S[job_m].append(job)
                end_times.increase_key(1, PQ_Entry(job, job_m))
                # minimum in PQ is at index 1 - increase that key with new job
                scheduled = True
            else:
                print(f'Cannot schedule job on existing machines')
        if not scheduled: # need new machine
            m += 1
            print(f'Schedule job on new machine {m}')
            S.append([job])
            end_times.insert_key(PQ_Entry(job, m))
    return S

def print_schedule(S):
    print('Schedule for each machine:')
    for m, jobs in enumerate(S[1:], start = 1):
        print(f'machine {m}:')
        for job in jobs: print(job)

def test_job_scheduling():
    print('Example from lecture 19 slides 31/32')
    jobs = job_examples.example1
    S = schedule(jobs)
    print_schedule(S)

    print('\n\nExample from lecture 20 slide 30')
    jobs = job_examples.example2
    S = schedule(jobs)
    print_schedule(S)

    print('\n\nExample 3')
    jobs = job_examples.example3
    S = schedule(jobs)
    print_schedule(S)

if __name__ == '__main__':
    test_job_scheduling()