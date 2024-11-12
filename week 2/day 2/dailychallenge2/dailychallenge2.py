class Pagination:
    def __init__(self, items=[], pageSize=10):
        self.currentPage=pageSize
        self.totalPages=(len(self.items)/self.pageSize)+1
    def getVisibleItems(self):
        print(self.items[self.currentPage - self.pageSize: self.currentPage])
    def firstPage(self):
        self.currentPage=self.pageSize
    def nextPage(self):
        if self.currentPage<len(self.items):
            self.currentPage+=self.pageSize
        return self.currentPage
    def prevPage(self):
        if self.currentPage>self.pageSize:
            self.currentPage -=self.pageSize
        return self.currentPage
    def lastPage(self):
        if self.totalPages %1 !=0:
            lastpage=int(self.totalPages)*self.pageSize
        else:
            lastpage=len(self.items)
        
        self.currentPage=lastpage
        return self.currentPage
    def goToPage(self,pageNum):
        if pageNum>int(self.totalPages):
            self.currentPage =int(self.totalPages)*self.pageSize
        else:
            self.currentPage= pageNum*self.pageSize
        return self.currentPage