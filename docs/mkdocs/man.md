# Man Page

`lsutil [options]`

## Syntax

`--long`

: use a long listing format

`--all`

: show entries starting with '.', except for '.' and '..'

`-1`, `--one`:

: show one line per entry

`--formats`:

: use a format string to print entry. See Formatting the Output below


## Formating the Output

The format string FORMAT controls the contents of the time output.  The format string can be set using the `-f' or
`--format', `-v' or `--verbose', or `-p' or `--portability' options.  If they are not given, but the TIME
environment variable is set, its value is used as the format string.  Otherwise, a built-in default format is used.
The default format is:
 %Uuser %Ssystem %Eelapsed %PCPU (%Xtext+%Ddata %Mmax)k
 %Iinputs+%Ooutputs (%Fmajor+%Rminor)pagefaults %Wswaps

The format string usually consists of `resource specifiers' interspersed with plain text.  A percent sign (`%') in
the format string causes the following character to be interpreted as a resource specifier, which is similar to the
formatting characters in the printf(3) function.

A backslash (`\') introduces a `backslash escape', which is translated into a single printing character upon
output.  `\t' outputs a tab character, `\n' outputs a newline, and `\\' outputs a backslash.  A backslash followed
by any other character outputs a question mark (`?') followed by a backslash, to indicate that an invalid backslash
escape was given.

Other text in the format string is copied verbatim to the output.


time always prints a newline after printing the
resource use information, so normally format strings do not end with a newline character (or `\n').

There are many resource specifications.  Not all resources are measured by all versions of Unix, so some of the
values might be reported as zero.  Any character following a percent sign that is not listed in the table below
causes a question mark (`?') to be output, followed by that character, to indicate that an invalid resource
specifier was given.

The resource specifiers, which are a superset of those recognized by the tcsh(1) builtin `time' command, are:

      %      A literal `%'.
      C      Name and command line arguments of the command being timed.
      D      Average size of the process's unshared data area, in Kilobytes.
      E      Elapsed real (wall clock) time used by the process, in [hours:]minutes:seconds.
      F      Number of major, or I/O-requiring, page faults that occurred while the process was running.  These
             are faults where the page has actually migrated out of primary memory.
      I      Number of file system inputs by the process.
      K      Average total (data+stack+text) memory use of the process, in Kilobytes.
      M      Maximum resident set size of the process during its lifetime, in Kilobytes.
      O      Number of file system outputs by the process.
      P      Percentage of the CPU that this job got.  This is just user + system times divided by the total
             running time.  It also prints a percentage sign.

## Examples

To run the command `wc /etc/hosts' and show the default information:

    time wc /etc/hosts

To run the command `ls -Fs' and show just the user, system, and total time:

    time -f "\t%E real,\t%U user,\t%S sys" ls -Fs

To edit the file BORK and have `time' append the elapsed time and number of signals to the file `log', reading the
format string from the environment variable `TIME':

    export TIME="\t%E,\t%k" # If using bash or ksh
    setenv TIME "\t%E,\t%k" # If using csh or tcsh
    time -a -o log emacs bork

Users of the bash shell need to use an explicit path in order to run the external time command and not the shell
builtin variant.  On system where time is installed in /usr/bin, the first example would become

    /usr/bin/time wc /etc/hosts

## ACCURACY

   The elapsed time is not collected atomically with the execution of the program; as a result, in bizarre
   circumstances (if the time command gets stopped or swapped out in between when the program being timed exits and
   when time calculates how long it took to run), it could be much larger than the actual execution time.

   When the running time of a command is very nearly zero, some values (e.g., the percentage of CPU used) may be
   reported as either zero (which is wrong) or a question mark.

   Most information shown by time is derived from the wait3(2) system call.  The numbers are only as good as those
   returned by wait3(2).  On systems that do not have a wait3(2) call that returns status information, the times(2)
   system call is used instead.  However, it provides much less information than wait3(2), so on those systems time
   reports the majority of the resources as zero.

   The `%I' and `%O' values are allegedly only `real' input and output and do not include those supplied by caching
   devices.  The meaning of `real' I/O reported by `%I' and `%O' may be muddled for workstations, especially diskless
   ones.

## DIAGNOSTICS

   The time command returns when the program exits, stops, or is terminated by a signal.  If the program exited
   normally, the return value of time is the return value of the program it executed and measured.  Otherwise, the
   return value is 128 plus the number of the signal which caused the program to stop or terminate.

## AUTHOR

   time was written by David MacKenzie.  This man page was added by Dirk Eddelbuettel <edd@debian.org>, the Debian
   GNU/Linux maintainer, for use by the Debian GNU/Linux distribution but may of course be used by others.

## See Also
   ls(1)
