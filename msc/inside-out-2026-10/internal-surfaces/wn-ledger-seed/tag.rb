require 'json'
items=JSON.parse(File.read("items.json"),symbolize_names:true)
main=items.reject{|i| i[:sec]=~/gold|Candidate|Follow-up|Belongs|Readers|figures|Brief|Teaching|fresh reader/i}
def tag(t)
  h=t[0,160]
  tags=[]
  tags<<"resolved" if h=~/\b(Resolved|RESOLVED|CHARACTERIZED|Closed|CLOSED|Landed|LANDED|Done|DONE)\b|~~/ 
  tags<<"open" if h=~/\b(Open|OPEN|Unresolved|open question|Open question|TODO|Gap|GAP|Conjecture|conjecture|Queued|queued)\b/
  tags<<"partial" if h=~/\bPartial\b/
  tags<<"neurips" if t=~/NeurIPS/
  tags<<"migration" if h=~/Migration note|Provenance|Segment split|Landing context|Trail\.|History/
  tags<<"memorata/upstream" if h=~/memorata|Upstream files|Internal references|Discovered via/
  tags<<"cite-deferred" if t=~/\[\^(cat|bg2|cite)[^\]]*\]|verification-deferred|Track E surface-back/
  tags<<"naming" if h=~/Naming|naming/
  tags<<"promo-block" if h=~/Promotion-blocking|Open before .candidate|Open questions for verification/
  tags<<"spike-ptr" if t=~/spikes\//
  tags<<"audit-ptr" if t=~/audits\/|AUDIT-WORKING|audit-findings/
  tags<<"msc-ptr" if t=~/msc\//
  tags<<"tracker-ptr" if t=~/TODO\.md|PROPOSALS|PROPOSED|TST-IDEAS|SP-\d+/
  tags<<"regression-guard" if h=~/[Rr]egression/
  tags<<"math" if t.scan(/\$/).size>=12
  tags
end
main.each{|i| i[:tags]=tag(i[:text])}
File.write("main.json",JSON.pretty_generate(main))
c=Hash.new{|h,k|h[k]=[0,0]}
main.each{|i| (i[:tags].empty? ? ["untagged"] : i[:tags]).each{|t| c[t][0]+=1; c[t][1]+=i[:chars]}}
puts "main items #{main.size} chars #{main.sum{|i|i[:chars]}}"
c.sort_by{|k,v|-v[1]}.each{|k,v| puts "#{k}\t#{v[0]}\t#{v[1]}"}
