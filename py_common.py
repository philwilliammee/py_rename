import os
import sys
from distutils.dir_util import copy_tree
import shutil
import stat

def del_evenReadonly(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

def appendInstallFields(fp, en, fields):
  f = open( fp , 'a+')
  s = en+':'
  for field in fields:
    s +="""
{0}: {1}""".format(field[0], field[1])
  f.write(s)
  f.close()

def appendSchemaFields(fp, fields):
  f = open( fp , 'a+')
  s=''
  for field in fields:
    s +="""
    {0}:
      type: string
      label: '{0}'""".format(field)
  f.write(s)
  f.close()

def appendForm(fp, fields):
  f = open(fp, "r")
  contents = f.readlines()
  f.close()
  #// Additional form elements for your custom properties.
  s = ""
  s2 = ""
  for field in fields:
    s +="""
    $form['{0}'] = [
      '#type' => 'textfield',
      '#title' => $this->t("content {0} field"),
      '#default_value' => $config->get('{0}'),
      '#description' => $this->t("Mapping: field machine name for the source {0}"),
      '#required' => FALSE,
    ];
    """.format(field)

    s2 +="""
      ->set('{0}', $form_state->getValue('{0}'))""".format(field)

  index = -1
  setIndex = -1
  for i, content in enumerate(contents):
    # print(i, content)
    if ('ADITIONAL' in content):
      index = i+1
    elif('SET form' in content):
      setIndex = i+1
  #index = contents.index('    // ADITIONAL form elements for your custom properties.')

  contents.insert(index, s)
  contents.insert(setIndex, s2)
  f = open(fp, "w")
  contents = "".join(contents)
  f.write(contents)
  f.close()

