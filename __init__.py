import datetime as dt
from subprocess import run, PIPE

from ranger.api.commands import Command

def duration(filename: str) -> str:
    video = '"' + filename + '"'
    cmd = "ffmpeg -i " + video + " 2>&1 | grep Duration | cut -d ' ' -f 4 | sed s/,//"
    output = run(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    return str(output.stdout, 'UTF-8').rstrip('\n')

def parse_delta(entry):
    import datetime
    h, m, s = entry.split(':')
    return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(float(s)))

def duration_sum(timetable: list) -> str:
    import datetime
    time_sum = datetime.timedelta()
    delta_times = list(map(parse_delta, timetable))
    for time in delta_times:
        time_sum += time
    return time_sum

class vuration(Command):
    def execute(self):
        if self.arg(1):
            video_file = self.rest(1)
        if self.fm.thisdir.marked_items:
            video_file = [f.relative_path for f in self.fm.thistab.get_selection()]
            timetable = list(map(duration,video_file))
            self.fm.notify(duration_sum(timetable))
        else:
            video_file = self.fm.thisfile.path
            self.fm.notify(duration(video_file))
