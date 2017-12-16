pijiu = 2.0
qian = 10.0
i = 0
gaizicount = 0
pingzicount = 0
while qian >= pijiu:
    qian -= pijiu
    i+=1
    gaizicount+=1
    pingzicount+=1
    print '第%d瓶啤酒，剩余%f钱,盖子数量%d,瓶子数量%d' % (i, qian, gaizicount, pingzicount)
    if gaizicount==4:
        qian += pijiu
        gaizicount = 0
        print '换盖子，第%d瓶啤酒，剩余%f钱,盖子数量%d,瓶子数量%d' % (i, qian, gaizicount, pingzicount)
    if pingzicount==2:
        qian += pijiu
        pingzicount = 0
        print '换瓶子，第%d瓶啤酒，剩余%f钱,盖子数量%d,瓶子数量%d' % (i, qian,gaizicount,pingzicount)