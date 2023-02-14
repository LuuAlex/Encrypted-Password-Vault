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
    
    init(array: [String]) {
        self.key = array[0]
        self.user = array[1]
        self.pass = array[2]
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

