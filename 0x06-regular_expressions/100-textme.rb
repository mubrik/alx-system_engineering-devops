#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=flags:|from:|to:)[^\]]+/).join(',')
