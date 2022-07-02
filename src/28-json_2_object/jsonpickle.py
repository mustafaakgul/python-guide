import jsonpickle

labeled_images_pickled = jsonpickle.encode(labeled_images)
labeled_imaged_unpickled = jsonpickle.decode(labeled_images_pickled)