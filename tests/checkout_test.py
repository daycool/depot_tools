sys.path.insert(0, os.path.dirname(ROOT_DIR))

from testing_support import fake_repos
from testing_support.patches_data import GIT, RAW
BAD_PATCH = ''.join(
    [l for l in GIT.PATCH.splitlines(True) if l.strip() != 'e'])
    self._commit_svn(self._tree_1())
    self._commit_svn(self._tree_2())

  @staticmethod
  def _tree_1():
    fs['trunk/chrome/file.cc'] = (
    return fs

  @classmethod
  def _tree_2(cls):
    fs = cls._tree_1()
    fs['trunk/chromeos/views/DOMui_menu_widget.h'] = (
      '// Copyright (c) 2010\n'
      '// Use of this source code\n'
      '// found in the LICENSE file.\n'
      '\n'
      '#ifndef DOM\n'
      '#define DOM\n'
      '#pragma once\n'
      '\n'
      '#include <string>\n'
      '#endif\n')
    return fs
  is_read_only = False
        patch.FilePatchDiff('new_dir/subdir/new_file', GIT.NEW_SUBDIR, []),
        patch.FilePatchDiff('chrome/file.cc', GIT.PATCH, []),
      content_lines = tree['chrome/file.cc'].splitlines(True)
      tree['chrome/file.cc'] = ''.join(
    self.assertEquals(not read_only, bool(expected))
    self.assertEquals(read_only, self.is_read_only)
        ['bin_file', 'chrome/file.cc', 'new_dir/subdir/new_file', 'extra'],
        patches.filenames)
          co._branches())
      co.apply_patch([patch.FilePatchDiff('chrome/file.cc', BAD_PATCH, [])])
      self.assertEquals(e.filename, 'chrome/file.cc')
    expected_co = getattr(co, 'checkout', co)
    # Because of ReadOnlyCheckout.
    expected = [(expected_co, p) for p in ps.patches]
    self.assertEquals(len(expected), len(results))
  def _check_move(self, co):
    """Makes sure file moves are handled correctly."""
    co.prepare(None)
    patchset = patch.PatchSet([
        patch.FilePatchDelete('chromeos/views/DOMui_menu_widget.h', False),
        patch.FilePatchDiff(
          'chromeos/views/webui_menu_widget.h', GIT.RENAME_PARTIAL, []),
    ])
    co.apply_patch(patchset)
    # Make sure chromeos/views/DOMui_menu_widget.h is deleted and
    # chromeos/views/webui_menu_widget.h is correctly created.
    root = os.path.join(self.root_dir, self.name)
    tree = self.get_trunk(False)
    del tree['chromeos/views/DOMui_menu_widget.h']
    tree['chromeos/views/webui_menu_widget.h'] = (
        '// Copyright (c) 2011\n'
        '// Use of this source code\n'
        '// found in the LICENSE file.\n'
        '\n'
        '#ifndef WEB\n'
        '#define WEB\n'
        '#pragma once\n'
        '\n'
        '#include <string>\n'
        '#endif\n')
    #print patchset[0].get()
    #print fake_repos.read_tree(root)
    self.assertTree(tree, root)

  def _get_co(self, post_processors):
    self.assertNotEqual(False, post_processors)
    return checkout.SvnCheckout(
        self.root_dir, self.name, self.usr, self.pwd, self.svn_url,
        post_processors)
  def testAll(self):
    root = os.path.join(self.root_dir, self.name)
    self._check_base(self._get_co(None), root, False, expected)
        self._get_co(None),
        'patching file chrome/file.cc\n'
        'chrome/file.cc.rej\n')
    co = self._get_co(None)
          [patch.FilePatchDiff('chrome/file.cc', RAW.PATCH, svn_props)])
      self.assertEquals(e.filename, 'chrome/file.cc')
          'While running svn propset svn:ignore foo chrome/file.cc '
          'patching file chrome/file.cc\n'
          'svn: Cannot set \'svn:ignore\' on a file (\'chrome/file.cc\')\n')
        [patch.FilePatchDiff('chrome/file.cc', RAW.PATCH, svn_props)])
    filepath = os.path.join(self.root_dir, self.name, 'chrome/file.cc')
    root = os.path.join(self.root_dir, self.name)
    self._check_base(self._get_co(None), root, False, expected)
    co = self._get_co(None)
        ['bin_file', 'chrome/file.cc', 'new_dir/subdir/new_file', 'extra'],
        patches.filenames)
        ['svn', 'pget', 'svn:eol-style', 'chrome/file.cc'],
    self._test_process(self._get_co)
    self._test_prepare(self._get_co(None))

  def testMove(self):
    self._check_move(self._get_co(None))
  def _get_co(self, post_processors):
    self.assertNotEqual(False, post_processors)
    return checkout.GitSvnCheckout(
        self.svn_base, self.svn_trunk, post_processors)
  def testAll(self):
    root = os.path.join(self.root_dir, self.name)
    self._check_base(self._get_co(None), root, True, expected)
    git_svn_co = self._get_co(None)
        self._get_co(None), 'fatal: corrupt patch at line 12\n')
    co = self._get_co(None)
          [patch.FilePatchDiff('chrome/file.cc', RAW.PATCH, svn_props)])
      self.assertEquals(e.filename, 'chrome/file.cc')
          'Cannot apply svn property foo to file chrome/file.cc.')
        [patch.FilePatchDiff('chrome/file.cc', RAW.PATCH, svn_props)])
    self._test_process(self._get_co)
    co = self._get_co(None)
    # TODO(maruel): Cheat here until prepare(revision != None) implemented.
    co.old_prepare = co.prepare
    def prepare(rev):
      # Basically, test that it is broken.
      self.assertEquals(1, rev)
      self.assertEquals(2, co.old_prepare(None))
      return 1
    co.prepare = prepare
  def testMove(self):
    self._check_move(self._get_co(None))

  def _get_co(self, post_processors):
    self.assertNotEqual(False, post_processors)
    return checkout.RawCheckout(self.root_dir, self.name, post_processors)
  def testAll(self):
    # Can't use self._check_base() since it's too different.
    co = self._get_co(None)
        ['bin_file', 'chrome/file.cc', 'new_dir/subdir/new_file', 'extra'],
        patches.filenames)
    try:
      co.commit(u'msg', self.FAKE_REPOS.USERS[1][0])
      self.fail()
    except NotImplementedError:
      pass
  def testException(self):
    self._check_exception(
        self._get_co(None),
        'patching file chrome/file.cc\n'
        'Hunk #1 FAILED at 3.\n'
        '1 out of 1 hunk FAILED -- saving rejects to file '
        'chrome/file.cc.rej\n')

  def testProcess(self):
    self._test_process(self._get_co)

  def testPrepare(self):
    # RawCheckout doesn't support prepare() but emulate it.
    co = self._get_co(None)
    revs = [1]
    def prepare(asked):
      self.assertEquals(1, asked)
      return revs.pop(0)
    co.prepare = prepare
    self._test_prepare(co)
    self.assertEquals([], revs)

  def testMove(self):
    self._check_move(self._get_co(None))

class ReadOnlyCheckout(SvnBaseTest):
  # Use SvnCheckout as the backed since it support read-only checkouts too.
  is_read_only = True

  def _get_co(self, post_processors):
    self.assertNotEqual(False, post_processors)
    return checkout.ReadOnlyCheckout(
        checkout.SvnCheckout(
            self.root_dir, self.name, None, None, self.svn_url, None),
        post_processors)

  def testAll(self):
    root = os.path.join(self.root_dir, self.name)
    self._check_base(self._get_co(None), root, False, None)
        self._get_co(None),
        'While running patch -p1 --forward --force;\n'
        'patching file chrome/file.cc\n'
        'chrome/file.cc.rej\n')
    self._test_process(self._get_co)
    self._test_prepare(self._get_co(None))

  def testMove(self):
    self._check_move(self._get_co(None))