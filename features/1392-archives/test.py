from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='42e99f18e9fbcd64888dcb84c48b49df',
        args='--ar-index=100'
    )

    def test_check_for_some_currently_detected_functions(self):
        assert self.out_c.has_func( '_ZN16ObserverEventMap12getObserversEj' )
        assert self.out_c.has_func( '_ZN3sys4lang9ReferenceIPN6engine3ORB17DistributedObjectEED1Ev' )
        assert self.out_c.has_func( '_ZN3sys4util5EntryIjNS0_12SortedVectorIN6engine4core16ManagedReferenceIPNS3_4util8ObserverEEEEEE8getValueEv' )
        assert self.out_c.has_func( '_ZN3sys4util9ArrayListIN6engine4core16ManagedReferenceIPNS2_4util8ObserverEEEEC2ERKS9_' )
        assert self.out_c.has_func( '_ZN3sys4util9HashTableIjNS0_12SortedVectorIN6engine4core16ManagedReferenceIPNS3_4util8ObserverEEEEEE6removeERKj' )
        assert self.out_c.has_func( '_ZN6engine4core16ManagedReferenceIPNS_4util8ObserverEE14toBinaryStreamEPN3sys2io18ObjectOutputStreamE' )
        assert self.out_c.has_func( '_ZNK3sys4util12SortedVectorIPN6engine4util8ObserverEE7compareERS5_RKS5_' )
        assert self.out_c.has_func( '_ZNV3sys4lang27StrongAndWeakReferenceCount19increaseStrongCountEv' )
        assert self.out_c.has_func( '_ZThn20_N3sys4util6VectorIPN6engine4util8ObserverEED1Ev' )
