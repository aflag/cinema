# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.exporter import JsonLinesItemExporter


class NormalizePipeline(object):
    def process_item(self, item, spider):
        for key,value in item.items():
            item[key] = value.strip()
            if key != 'title':
                item[key] = ' '.join(value.lower().split())
        return item


class CinemaPipeline(object):
    def open_spider(self, spider):
        self.file = open('data/' + spider.name+'.jsonlines', 'a')
        self.exporter = JsonLinesItemExporter(self.file) 
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
