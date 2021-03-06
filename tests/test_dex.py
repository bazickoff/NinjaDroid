from os import listdir
from os.path import join
import unittest

from ninjadroid.parsers.dex import Dex
from ninjadroid.errors.parsing_error import ParsingError


class TestDex(unittest.TestCase):
    """
    UnitTest for dex.py.

    RUN: python -m unittest -v tests.test_dex
    """

    dex_properties = {
        "classes.dex": {
            "name": "classes.dex",
            "size": 2132,
            "md5": "7bc52ece5249ccd2d72c4360f9be2ca5",
            "sha1": "89476799bf92798047ca026c922a5bc33983b008",
            "sha256": "3f543c68c4c059548cec619a68f329010d797e5e4c00aa46cd34c0d19cabe056",
            "sha512": "0725f961bc1bac47eb8dd045c2f0a0cf5475fd77089af7ddc3098e341a95d8b5624969b6fa47606a05d5a6adf9d74d0c52562ea41a376bd3d7d0aa3695ca2e22",
            "strings": [
                "Lcom/example/app/ExampleService;",
                "!Lcom/example/app/ExampleService2;",
                "!Lcom/example/app/ExampleService3;",
                "#Landroid/content/BroadcastReceiver;",
                ")Lcom/example/app/ExampleBrodcastReceiver;",
                "*Lcom/example/app/ExampleBrodcastReceiver2;",
                "*Lcom/example/app/ExampleBrodcastReceiver3;",
                "*Lcom/example/app/ExampleBrodcastReceiver4;",
                "<init>",
                "Landroid/app/Activity;",
                "Landroid/app/Service;", "Landroid/content/Context;",
                "Landroid/content/Intent;",
                "Landroid/os/Bundle;",
                "Landroid/os/IBinder;",
                "Lcom/example/app/HomeActivity;",
                "Lcom/example/app/OtherActivity;",
                "onBind",
                "onCreate",
                "onReceive",
                "setContentView"],
            "urls": [],
            "shell_commands": ["set"],
            "custom_signatures": [],
        },
    }

    @classmethod
    def setUpClass(cls):
        cls.dexes = {}

        for file in listdir(join("tests", "data")):
            if file in cls.dex_properties:
                cls.dexes[file] = Dex(join("tests", "data", file), file)
                # print(cls.dexes[filename].dump())

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        for filename in self.dexes:
            # When:
            dex = self.dexes[filename]

            # Then:
            self.assertTrue(dex is not None)
            self.assertTrue(type(dex) is Dex)

        # Test the class raise when a non-existing file is given:
        with self.assertRaises(ParsingError):
            filename = "aaa_this_is_a_non_existent_file_xxx"
            Dex(join("tests", "data", filename), filename)

    def test_get_raw_file(self):
        for filename in self.dexes:
            # When:
            raw_file = self.dexes[filename].get_raw_file()

            # Then:
            self.assertTrue(len(raw_file) > 0)

    def test_get_file_name(self):
        for filename in self.dexes:
            # When:
            name = self.dexes[filename].get_file_name()

            # Then:
            self.assertEqual(self.dex_properties[filename]["name"], name)

    def test_get_size(self):
        for filename in self.dexes:
            # When:
            size = self.dexes[filename].get_size()

            # Then:
            self.assertEqual(self.dex_properties[filename]["size"], size)

    def test_get_md5(self):
        for filename in self.dexes:
            # When:
            md5 = self.dexes[filename].get_md5()

            # Then:
            self.assertEqual(self.dex_properties[filename]["md5"], md5)

    def test_get_sha1(self):
        for filename in self.dexes:
            # When:
            sha1 = self.dexes[filename].get_sha1()

            # Then:
            self.assertEqual(self.dex_properties[filename]["sha1"], sha1)

    def test_get_sha256(self):
        for filename in self.dexes:
            # When:
            sha256 = self.dexes[filename].get_sha256()

            # Then:
            self.assertEqual(self.dex_properties[filename]["sha256"], sha256)

    def test_get_sha512(self):
        for filename in self.dexes:
            # When:
            sha512 = self.dexes[filename].get_sha512()

            # Then:
            self.assertEqual(self.dex_properties[filename]["sha512"], sha512)

    def test_get_strings(self):
        for filename in self.dexes:
            # When:
            strings = self.dexes[filename].get_strings()

            # Then:
            self.assertEqual(set(self.dex_properties[filename]["strings"]), set(strings))

    def test_get_urls(self):
        for filename in self.dexes:
            # When:
            urls = self.dexes[filename].get_urls()

            # Then:
            self.assertEqual(self.dex_properties[filename]["urls"], urls)

    def test_get_shell_commands(self):
        for filename in self.dexes:
            # When:
            shell_commands = self.dexes[filename].get_shell_commands()

            # Then:
            self.assertEqual(self.dex_properties[filename]["shell_commands"], shell_commands)

    # def test_get_custom_signatures(self):
    #     for filename in self.dexes:
    #         # When:
    #         custom_signatures = self.dexes[filename].get_custom_signatures()
    #
    #         # Then:
    #         self.assertEqual(self.dex_properties[filename]["custom_signatures"], custom_signatures)


if __name__ == "__main__":
    unittest.main()
