def survey(name, age, **informations):
    informations["真实姓名"] = name
    informations['年龄'] = age
    return informations