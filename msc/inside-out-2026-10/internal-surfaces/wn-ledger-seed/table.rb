require 'json'
it=JSON.parse(File.read("items.json"))
tsv=File.readlines("all.txt.tsv").map{|l| l.chomp.split("\t")}
research=/prior-art search|Pillar|primary-source verification|relata|[Cc]itation verification|[Vv]erify the citation|verification-deferred|intuition-only|novelty search|Relata pass|queued with the BG2|BG2 cluster/
openre=/\b(Open|open question|Open question|not derived|unverified|[Cc]onjecture|is open|remains open|queued|Queued|not yet|unaddressed|Promotion-blocking|Open before)\b/
rows=tsv.map do |f,st,stg,n,d0,d1|
  its=it.select{|i| i["file"]==f}
  main=its.reject{|i| i["sec"]=~/gold|Candidate|Follow-up|Belongs|Readers|figures|Brief|Teaching|fresh reader|Off-ramp/i}
  slug=f.sub(/.*src\//,"").sub(".md","")
  gold= its.any?{|i| i["sec"]=~/gold/i} ? "y" : ""
  off= its.any?{|i| i["sec"]=~/Off-ramp/} ? "y" : ""
  nip= its.any?{|i| i["text"]=~/NeurIPS/} ? "y" : ""
  res= its.count{|i| i["text"]=~research && i["text"]!~/\A\[\^/}
  op= main.count{|i| i["text"][0,200]=~openre}
  gs= its.select{|i| i["sec"]!="main"}.sum{|i| i["chars"]}
  ms= main.sum{|i| i["chars"]}
  [f[0,2],slug,st,stg,n.to_i,d1,ms/1000,gs/1000,gold,off,nip,res,op]
end
rows.sort_by!{|r| [r[0], -(r[6]+r[7])]}
puts "| vol | slug | status | stage | WN lines | WN last touched | theory-state kchars | gold/off-ramp kchars | gold | off-ramp | NeurIPS | owed-research items | open-flagged items |"
puts "|---|---|---|---|---|---|---|---|---|---|---|---|---|"
rows.each{|r| puts "| #{r[0]} | `#{r[1]}` | #{r[2]} | #{r[3]} | #{r[4]} | #{r[5]} | #{r[6]} | #{r[7]} | #{r[8]} | #{r[9]} | #{r[10]} | #{r[11]==0 ? "" : r[11]} | #{r[12]==0 ? "" : r[12]} |"}
