module Jekyll
    class HeatmapTag < Liquid::Tag
	def initialize(tag_name, input, tokens)
	    super
	end

	def render(context)
	    `python3 ./measure_zettels_progress.py`
	end
    end
end

Liquid::Template.register_tag('heatmap', Jekyll::HeatmapTag)
