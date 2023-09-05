#!/usr/bin/env ruby
#a ruby script containing a regex that natches hbtnnn

puts ARGV[0].scan(/hbt{2,5}n/).join
