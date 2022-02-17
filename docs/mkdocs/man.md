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

(Copied from time command, not correct for lsutil)

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




## See Also
   ls(1)
