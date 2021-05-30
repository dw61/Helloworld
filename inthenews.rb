require 'inthenews'

@news = InTheNews::Parser.new
items = @news.items

puts items.first.text
puts items.first.topics
