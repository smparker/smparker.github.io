abort('Please run this using `bundle exec rake`') unless ENV["BUNDLE_BIN_PATH"]
require 'html-proofer'

desc 'Build site with Jekyll.'
task :build  do
	print "Compiling website...\n"
  sh "jekyll build"
end

desc "Test the website"
task :test => [:build] do
  options = {
    :check_html => true,
    :check_favicon => true,
    :check_img_http => true,
    :check_opengraph => true,
    :empty_alt_ignore => false,
    :enforce_https => true,
    :url_ignore => ['https://scholar.google.com/citations?user=OqC2Vc8AAAAJ&hl=en'],
    :url_swap => { 'https://quantumparker.com' => '' },
    :cache => {
      :timeframe => '6w'
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
