from leapp.actors import Actor
from leapp.models import UpgradeDracutModule
from leapp.tags import FactsPhaseTag, IPUWorkflowTag


class AddDracutDebugModule(Actor):
    """
    No documentation has been provided for the add_dracut_debug_module actor.
    """

    name = 'add_dracut_debug_module'
    consumes = ()
    produces = (UpgradeDracutModule,)
    tags = (FactsPhaseTag, IPUWorkflowTag)

    def process(self):
        self.produce(UpgradeDracutModule(
            name='leapp-debug',
            module_path=self.get_actor_folder_path('dracut/84leapp-debug')
        ))
