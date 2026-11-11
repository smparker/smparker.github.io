abort('Please run this using `bundle exec rake`') unless ENV["BUNDLE_BIN_PATH"]
require 'html-proofer'

desc 'Build site with Jekyll.'
task :build  do
	print "Compiling website...\n"
  sh "jekyll build"
end

desc "Test the website"
task :test => [:build] do
  # html-proofer 5.x options
  options = {
    :checks => ['Links', 'Images', 'Scripts', 'Favicon', 'OpenGraph'],
    :ignore_empty_alt => false,
    :enforce_https => true,
    :ignore_urls => ['https://scholar.google.com/citations?user=OqC2Vc8AAAAJ&hl=en'],
    :swap_urls => { %r{^https://quantumparker\.com} => '' },
    :cache => {
      :timeframe => { :external => '6w' }
    },
    :typhoeus => {
      :timeout => 500
    }
  }
  begin
    HTMLProofer.check_directory("_site/", options).run
  rescue => msg
    puts "#{msg}"
  end
end

task :default => [:test]
