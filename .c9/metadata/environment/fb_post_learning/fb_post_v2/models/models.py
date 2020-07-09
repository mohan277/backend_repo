{"filter":false,"title":"models.py","tooltip":"/fb_post_learning/fb_post_v2/models/models.py","undoManager":{"mark":21,"position":21,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":2},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"insert","lines":["# "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"insert","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"insert","lines":["# "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"insert","lines":["# "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"insert","lines":["# "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":15,"column":0},"end":{"row":46,"column":38},"action":"insert","lines":["# models.py","class Group(models.Model):","    name = models.CharField()","","class User(models.Model):","    name = models.CharField()","    groups = models.ManyToManyField(Group)","","","# factories.py","class GroupFactory(factory.django.DjangoModelFactory):","    class Meta:","        model = models.Group","","    name = factory.Sequence(lambda n: \"Group #%s\" % n)","","class UserFactory(factory.django.DjangoModelFactory):","    class Meta:","        model = models.User","","    name = \"John Doe\"","","    @factory.post_generation","    def groups(self, create, extracted, **kwargs):","        if not create:","            # Simple build, do nothing.","            return","","        if extracted:","            # A list of groups were passed in, use them","            for group in extracted:","                self.groups.add(group)"],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"remove","lines":["# "],"id":5}],[{"start":{"row":1,"column":0},"end":{"row":13,"column":0},"action":"remove","lines":["","# from fb_post_v2.models.user import User","","","# class Post(models.Model):","#     user = models.ForeignKey(User, on_delete=models.CASCADE,","#                              related_name='posts')","#     posted_at = models.DateTimeField(auto_now=True)","#     post_content = models.CharField(max_length=250)","","#     def __str__(self):","#         return \"%s %s\" % (self.user, self.post_content)",""],"id":6}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":8},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":9},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["f"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["a"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["c"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":7},"end":{"row":0,"column":11},"action":"remove","lines":["fact"],"id":10},{"start":{"row":0,"column":7},"end":{"row":0,"column":14},"action":"insert","lines":["factory"]}],[{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":[","],"id":11}],[{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":[" "],"id":12},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["f"]},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["a"]},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["c"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":16},"end":{"row":0,"column":20},"action":"remove","lines":["fact"],"id":13},{"start":{"row":0,"column":16},"end":{"row":0,"column":23},"action":"insert","lines":["factory"]}],[{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":["."],"id":14},{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":["d"]}],[{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"remove","lines":["d"],"id":15},{"start":{"row":0,"column":24},"end":{"row":0,"column":30},"action":"insert","lines":["django"]}],[{"start":{"row":16,"column":16},"end":{"row":16,"column":23},"action":"remove","lines":["models."],"id":16}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":23},"action":"remove","lines":["models."],"id":17}],[{"start":{"row":28,"column":22},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":29,"column":0},"end":{"row":29,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"insert","lines":["g"],"id":19},{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"insert","lines":["r"]},{"start":{"row":29,"column":14},"end":{"row":29,"column":15},"action":"insert","lines":["o"]}],[{"start":{"row":29,"column":12},"end":{"row":29,"column":15},"action":"remove","lines":["gro"],"id":20},{"start":{"row":29,"column":12},"end":{"row":29,"column":17},"action":"insert","lines":["group"]}],[{"start":{"row":29,"column":17},"end":{"row":29,"column":18},"action":"insert","lines":[" "],"id":21},{"start":{"row":29,"column":18},"end":{"row":29,"column":19},"action":"insert","lines":["="]}],[{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"insert","lines":[" "],"id":22},{"start":{"row":29,"column":20},"end":{"row":29,"column":21},"action":"insert","lines":["G"]},{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"insert","lines":["r"]}],[{"start":{"row":29,"column":20},"end":{"row":29,"column":22},"action":"remove","lines":["Gr"],"id":23},{"start":{"row":29,"column":20},"end":{"row":29,"column":34},"action":"insert","lines":["GroupFactory()"]}]]},"ace":{"folds":[],"scrolltop":28,"scrollleft":0,"selection":{"start":{"row":36,"column":38},"end":{"row":36,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":67,"mode":"ace/mode/python"}},"timestamp":1593096062268,"hash":"cda0a59c15ebb91732e4eb0da2d0931f06dcec35"}