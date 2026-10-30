out = ARGV[0]
rows = []
Dir.glob("0[1-4]-*-core/src/*.md").sort.each do |f|
  lines = File.readlines(f)
  fm = lines.take_while.with_index{|l,i| i==0 || l !~ /^---/ }.join
  status = fm[/^status:\s*(\S+)/,1]; stage = fm[/^stage:\s*(\S+)/,1]
  s = lines.index{|l| l =~ /^## Working Notes/}
  next unless s
  e = (s+1...lines.size).find{|i| lines[i] =~ /^## / } || lines.size
  body = lines[s...e]
  # blame dates for WN lines
  bl = `git blame --line-porcelain -L #{s+1},#{e} -- "#{f}" 2>/dev/null`
  dates = bl.scan(/^author-time (\d+)/).flatten.map{|t| Time.at(t.to_i).strftime("%Y-%m-%d")}
  rows << [f, status, stage, body.size, dates.min, dates.max, body.join]
end
File.open(out,"w"){|io| rows.each{|r| io.puts "=====FILE #{r[0]} | status=#{r[1]} stage=#{r[2]} | wn_lines=#{r[3]} | blame #{r[4]}..#{r[5]}"; io.puts r[6]}}
File.open(out+".tsv","w"){|io| rows.each{|r| io.puts r[0..5].join("\t")}}
