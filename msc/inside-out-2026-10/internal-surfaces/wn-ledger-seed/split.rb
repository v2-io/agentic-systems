require 'json'
txt=File.read("all.txt"); parts=txt.split(/^=====FILE /)[1..]
items=[]
parts.each do |p|
  head,*body=p.lines
  f=head.split(" | ").first
  sec="main"
  cur=nil
  body.each do |l|
    next if l=~/^## Working Notes/
    if l=~/^###+\s+(.*)/
      sec=$1.strip; items<<cur if cur; cur=nil; next
    end
    if l=~/^- / || (l=~/^\S/ && cur.nil?) || (l=~/^\S/ && cur && cur[:text]=~/\n\s*\n\z/)
      items<<cur if cur
      cur={file:f, sec:sec, text:l.dup}
    else
      (cur ||= {file:f, sec:sec, text:""})[:text] << l
    end
  end
  items<<cur if cur
end
items.reject!{|i| i[:text].strip.empty?}
items.each_with_index{|it,i| it[:id]=i; it[:chars]=it[:text].size}
File.write("items.json", JSON.pretty_generate(items))
gold=items.select{|i| i[:sec]=~/gold/i}
puts "items #{items.size}  chars #{items.sum{|i|i[:chars]}}"
puts "gold-section items #{gold.size} chars #{gold.sum{|i|i[:chars]}} files #{gold.map{|i|i[:file]}.uniq.size}"
secs=Hash.new(0); items.each{|i| secs[i[:sec].sub(/\(.*$/,'').sub(/\d{4}-\d\d-\d\d/,'')[0,50]]+=i[:chars]}
secs.sort_by{|k,v|-v}.first(40).each{|k,v| puts "#{v}\t#{k}"}
