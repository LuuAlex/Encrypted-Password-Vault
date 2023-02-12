//
//  hashmap.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/12/23.
//

import Foundation

class DataObject {
    private var key: String
    private var user: String
    private var pass: String
    
    init(key: String, user: String, pass: String) {
        self.key = key
        self.user = user
        self.pass = pass
    }
    
    func getKey() -> String {
        return key
    }
    func getUser() -> String {
        return user
    }
    func getPass() -> String {
        return pass
    }
}

