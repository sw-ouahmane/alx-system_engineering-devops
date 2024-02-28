#!/usr/bin/env ruby
flags = ARGV[0].scan(/flags:(.*?)\]/)
from = ARGV[0].scan(/from:(.*?)\]/)
to = ARGV[0].scan(/to:(.*?)\]/)
puts [from, to, flags].join(',')